'use strict';

const scope = new URL(self.registration.scope);
const cachePrefix = `ba-battle:${scope.href}:`;
const cacheName = cachePrefix + 'v42.5';
const appFiles = ['index.html', 'manifest.webmanifest', 'icon-192.png', 'icon-512.png']
  .map(file => new URL(file, scope));
const page = appFiles[0].href;
const cachedPaths = new Set(appFiles.map(file => file.pathname));

self.addEventListener('install', event => {
  event.waitUntil((async () => {
    const cache = await caches.open(cacheName);
    await cache.addAll(appFiles.map(file => new Request(file, {cache: 'reload'})));
    await self.skipWaiting();
  })());
});

self.addEventListener('activate', event => {
  event.waitUntil((async () => {
    const keys = await caches.keys();
    await Promise.all(keys.filter(key => key.startsWith(cachePrefix) && key !== cacheName)
      .map(key => caches.delete(key)));
    await self.clients.claim();
  })());
});

self.addEventListener('fetch', event => {
  const {request} = event;
  const url = new URL(request.url);
  if (request.method !== 'GET' || url.origin !== scope.origin) return;

  if (request.mode === 'navigate' && (url.pathname === scope.pathname || url.pathname === appFiles[0].pathname)) {
    event.respondWith((async () => {
      try {
        return await fetch(request);
      } catch {
        return (await caches.open(cacheName)).match(page);
      }
    })());
  } else if (cachedPaths.has(url.pathname)) {
    event.respondWith((async () => {
      const cached = await (await caches.open(cacheName)).match(request, {ignoreSearch: true});
      return cached ?? fetch(request);
    })());
  }
});
