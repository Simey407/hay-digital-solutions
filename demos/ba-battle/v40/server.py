"""Same-origin Ba’ Battle account tester. Run with Python 3.9+ with SQLite 3.35+."""
import argparse
from contextlib import closing
import hashlib
import hmac
from http.cookies import SimpleCookie, CookieError
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
import json
from pathlib import Path
import re
import secrets
import sqlite3
import time
from urllib.parse import urlsplit

ROOT = Path(__file__).resolve().parent
SESSION_AGE = 14 * 86400
PROFILE = 'nickname, team, crest, trim'
ASSETS = {
    'index.html': 'text/html; charset=utf-8',
    'manifest.webmanifest': 'application/manifest+json',
    'sw.js': 'text/javascript',
    'icon-192.png': 'image/png',
    'icon-512.png': 'image/png',
}
BOARDS = {
    'wins': ('sum(m.won)', 'DESC'),
    'streak': ('max(m.streak)', 'DESC'),
    'score': ('max(m.score)', 'DESC'),
    'fastest': ('min(CASE WHEN m.won THEN m.seconds END)', 'ASC'),
}
SCHEMA = """
CREATE TABLE IF NOT EXISTS accounts(
 id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT UNIQUE COLLATE NOCASE NOT NULL,
 nickname TEXT UNIQUE COLLATE NOCASE NOT NULL, password BLOB NOT NULL, salt BLOB NOT NULL,
 team TEXT NOT NULL CHECK(team IN ('up','down')),
 crest TEXT NOT NULL DEFAULT 'ba', trim TEXT NOT NULL DEFAULT 'gold'
);
CREATE TRIGGER IF NOT EXISTS immutable_team BEFORE UPDATE OF team ON accounts
 WHEN OLD.team != NEW.team BEGIN SELECT RAISE(ABORT, 'Team is permanent'); END;
CREATE TABLE IF NOT EXISTS sessions(
 token TEXT PRIMARY KEY, account INTEGER NOT NULL REFERENCES accounts(id) ON DELETE CASCADE,
 expires INTEGER NOT NULL
);
CREATE TABLE IF NOT EXISTS matches(
 ticket TEXT PRIMARY KEY, account INTEGER NOT NULL REFERENCES accounts(id) ON DELETE CASCADE,
 started INTEGER NOT NULL, seconds INTEGER, won INTEGER, score INTEGER, streak INTEGER
);
CREATE INDEX IF NOT EXISTS match_account ON matches(account);
CREATE TABLE IF NOT EXISTS attempts(ip TEXT PRIMARY KEY, minute INTEGER NOT NULL, count INTEGER NOT NULL);
"""


class Problem(Exception):
    pass


def require(condition, message, status=400):
    if not condition:
        raise Problem(status, message)


def hash_password(password, salt):
    return hashlib.pbkdf2_hmac("sha256", password.encode(), salt, 600_000)


def digest(token):
    return hashlib.sha256(token.encode()).hexdigest()


def connect(path):
    db = sqlite3.connect(path)
    db.row_factory = sqlite3.Row
    db.execute('PRAGMA foreign_keys=ON')
    return db


def nickname(data):
    name = data.get('nickname', '')
    require(isinstance(name, str) and re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9 _’'-]{1,19}", name)
            and name == name.strip(), 'Use 2–20 letters, numbers, spaces or simple punctuation.')
    return name


class Handler(BaseHTTPRequestHandler):
    def setup(self):
        super().setup()
        self.connection.settimeout(10)

    def reply(self, status, data, content='application/json', cookie=None):
        if not isinstance(data, bytes):
            data = json.dumps(data).encode()
        self.send_response(status)
        self.send_header('Content-Type', content)
        self.send_header('Content-Length', str(len(data)))
        self.send_header('Cache-Control', 'no-store')
        self.send_header('X-Content-Type-Options', 'nosniff')
        if cookie:
            self.send_header('Set-Cookie', cookie)
        self.end_headers()
        self.wfile.write(data)

    def do_GET(self):
        path = urlsplit(self.path).path
        asset = 'index.html' if path == '/' else path.lstrip('/')
        if asset in ASSETS:
            return self.reply(200, (ROOT / asset).read_bytes(), ASSETS[asset])
        self.dispatch(path)

    def do_POST(self):
        self.dispatch(urlsplit(self.path).path, post=True)

    def dispatch(self, path, post=False):
        try:
            require(path.startswith('/api/'), 'Page unavailable.', 404)
            data = {}
            if post:
                require(self.headers.get('Origin') == self.server.origin, 'Request origin denied.', 403)
                length = self.headers.get('Content-Length', '')
                require(length.isascii() and length.isdigit() and len(length) < 5
                        and 0 < int(length) <= 2048 and self.headers.get_content_type() == 'application/json',
                        'Invalid request.')
                try:
                    data = json.loads(self.rfile.read(int(length)))
                except (ValueError, UnicodeError):
                    raise Problem(400, 'Invalid request.')
                require(isinstance(data, dict), 'Invalid request.')
            cookie = SimpleCookie()
            try:
                cookie.load(self.headers.get('Cookie', ''))
            except CookieError:
                pass
            token = digest(cookie['ba_session'].value) if 'ba_session' in cookie else ''
            with closing(connect(self.server.database)) as db:
                user = db.execute(f'''SELECT a.*, s.token FROM accounts a JOIN sessions s
                    ON s.account=a.id WHERE s.token=? AND s.expires>?''', (token, int(time.time()))).fetchone()
                if post and path in ('/api/signup', '/api/signin', '/api/delete'):
                    self.limit_auth(db)
                with db:
                    result, session = self.api(db, path, data, user, token, post)
            self.reply(200, result, cookie=session)
        except Problem as error:
            self.reply(error.args[0], {'error': error.args[1]})
        except sqlite3.IntegrityError:
            self.reply(409, {'error': 'That username or nickname is already in use.'})

    def limit_auth(self, db):
        minute = int(time.time()) // 60
        with db:
            db.execute('DELETE FROM attempts WHERE minute < ?', (minute,))
            count = db.execute('''INSERT INTO attempts VALUES(?,?,1)
                ON CONFLICT(ip) DO UPDATE SET count=count+1 RETURNING count''',
                (self.client_address[0], minute)).fetchone()[0]
        require(count <= 30, 'Too many attempts. Try again in a minute.', 429)

    def cookie(self, token='', age=0):
        secure = '; Secure' if self.server.origin.startswith('https://') else ''
        return f'ba_session={token}; Path=/; HttpOnly; SameSite=Strict; Max-Age={age}{secure}'

    def api(self, db, path, data, user, token, post):
        now = int(time.time())
        if not post:
            if path == '/api/session':
                return {'profile': {key: user[key] for key in ('nickname', 'team', 'crest', 'trim')} if user else None}, None
            if path.startswith('/api/boards/'):
                metric = path.rsplit('/', 1)[-1]
                require(metric in BOARDS, 'Unknown leaderboard.', 404)
                expression, order = BOARDS[metric]
                rows = db.execute(f'''SELECT {PROFILE}, {expression} AS value
                    FROM accounts JOIN matches m ON m.account=accounts.id WHERE m.seconds IS NOT NULL
                    GROUP BY accounts.id HAVING value IS NOT NULL AND value > 0
                    ORDER BY value {order}, nickname COLLATE NOCASE LIMIT 25''')
                return {'rows': [dict(row) for row in rows]}, None
            raise Problem(404, 'Page unavailable.')

        if path in ('/api/signup', '/api/signin', '/api/delete'):
            password = data.get('password')
            require(isinstance(password, str) and 12 <= len(password) <= 128
                    and not any(0xD800 <= ord(char) <= 0xDFFF for char in password),
                    'Enter a password of 12–128 characters.')
        if path in ('/api/signup', '/api/signin'):
            username = data.get('username', '')
            require(isinstance(username, str) and re.fullmatch('[A-Za-z0-9_]{3,24}', username),
                    'Use 3–24 letters, numbers or underscores for your username.')
            if path == '/api/signup':
                team = data.get('team')
                require(team in ('up', 'down'), 'Choose your permanent side.')
                name = nickname(data)
                require(name.casefold() != username.casefold(), 'Choose a different public nickname.')
                salt = secrets.token_bytes(16)
                account = db.execute('''INSERT INTO accounts(username,nickname,password,salt,team)
                    VALUES(?,?,?,?,?)''', (username, name, hash_password(password, salt), salt, team)).lastrowid
            else:
                existing = db.execute('SELECT * FROM accounts WHERE username=?', (username,)).fetchone()
                computed = hash_password(password, existing['salt'] if existing else bytes(16))
                require(existing and hmac.compare_digest(computed, existing['password']),
                        'Username or password is incorrect.', 401)
                account = existing['id']
            raw = secrets.token_urlsafe(32)
            db.execute('DELETE FROM sessions WHERE token=? OR expires<=?', (token, now))
            db.execute('INSERT INTO sessions VALUES(?,?,?)', (digest(raw), account, now+SESSION_AGE))
            profile = db.execute(f'SELECT {PROFILE} FROM accounts WHERE id=?', (account,)).fetchone()
            return {'profile': dict(profile)}, self.cookie(raw, SESSION_AGE)

        require(user is not None, 'Sign in to continue.', 401)
        account = user['id']
        if path == '/api/signout':
            db.execute('DELETE FROM sessions WHERE token=?', (token,))
            return {}, self.cookie()
        if path == '/api/delete':
            require(hmac.compare_digest(hash_password(password, user['salt']), user['password']),
                    'Password is incorrect.', 403)
            db.execute('DELETE FROM accounts WHERE id=?', (account,))
            return {}, self.cookie()
        if path == '/api/profile':
            require(set(data) == {'nickname', 'crest', 'trim'}, 'Team is permanent.')
            name, crest, trim = nickname(data), data['crest'], data['trim']
            require(name.casefold() != user['username'].casefold(), 'Choose a different public nickname.')
            require(crest in ('ba','wall','wave') and trim in ('gold','sea','heather'), 'Choose a listed style.')
            db.execute('UPDATE accounts SET nickname=?,crest=?,trim=? WHERE id=?', (name, crest, trim, account))
            return {'profile': dict(nickname=name, crest=crest, trim=trim, team=user['team'])}, None
        if path == '/api/match':
            require(data.get('team') == user['team'], 'Play for your permanent side.', 409)
            ticket = secrets.token_urlsafe(24)
            db.execute('DELETE FROM matches WHERE account=? AND seconds IS NULL', (account,))
            db.execute('INSERT INTO matches(ticket,account,started) VALUES(?,?,?)', (ticket, account, now))
            return {'ticket': ticket}, None
        if path == '/api/result':
            ticket, seconds, won, score, streak = (data.get(key) for key in ('ticket','seconds','won','score','streak'))
            require(isinstance(ticket, str) and type(won) is bool and type(seconds) is int
                    and 3 <= seconds <= 14400 and type(score) is int and 0 <= score <= 1000000
                    and type(streak) is int and 0 <= streak <= seconds * 5, 'Invalid match result.')
            saved = db.execute('''UPDATE matches SET seconds=?, won=?, score=?, streak=?
                WHERE ticket=? AND account=? AND seconds IS NULL AND started BETWEEN ? AND ?''',
                (seconds, won, score, streak, ticket, account, now-86400, now-max(0, seconds-5)))
            require(saved.rowcount == 1, 'Match ticket is expired, already used or unavailable.', 409)
            return {}, None
        raise Problem(404, 'Page unavailable.')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--port', type=int, default=8040)
    parser.add_argument('--database', type=Path, required=True, help='Path outside the repository')
    parser.add_argument('--origin', help='Exact HTTPS origin when fronted by a local TLS proxy')
    args = parser.parse_args()
    if args.origin and not re.fullmatch(r'https://[A-Za-z0-9.-]+(?::[0-9]+)?', args.origin):
        parser.error('--origin must be an HTTPS origin without a path')
    with closing(connect(args.database)) as db, db:
        db.executescript(SCHEMA)
    with ThreadingHTTPServer(('127.0.0.1', args.port), Handler) as server:
        server.database = args.database
        server.origin = args.origin or f'http://127.0.0.1:{args.port}'
        print(f'Ba’ Battle tester at {server.origin}', flush=True)
        server.serve_forever()
