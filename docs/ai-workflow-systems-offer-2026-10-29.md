# Hay Digital Solutions — AI Workflow Systems

Status: internal implementation brief  
Date: 29 October 2026  
Owner: Simon Hay  
Commercial status: do not publicly promote or sell until the existing BISE / secondary-business position allows it.

## Objective

Turn proven AI-implementation patterns into a practical Hay Digital capability for UK small businesses.

Hay Digital will not sell "AI teams" as a buzzword. It will sell measurable outcomes from one defined business workflow at a time.

The operating model is:

1. Identify one repetitive, costly or slow workflow.
2. Map the existing human process and systems.
3. Separate deterministic steps from judgement.
4. Use automation first where rules are enough.
5. Add AI/agents only where language, judgement or multi-step coordination adds value.
6. Keep human approval before sensitive or irreversible actions.
7. Test against real examples before production.
8. Measure time saved, errors, response time, conversion or cash impact.
9. Offer optional monitoring / care after launch.

## Market pattern we are adapting

Current UK providers consistently use a similar structure:

- free or low-friction workflow diagnosis;
- fixed-scope pilot;
- implementation inside tools the client already uses;
- human approval / hand-off for sensitive work;
- testing before wider rollout;
- optional monthly care / support.

Public examples reviewed in October 2026 include:

- Augustova — single automation £595 + optional £39/month; missed-call receptionist £695 + £79/month.
- Praxen AI — one workflow pilot around £2,030 launch pricing; care around £245/month; AI receptionist setup + monthly support.
- ZTech — lead-capture automation £495 + £79/month; website chatbot £595 + £99/month; AI receptionist £995 + £199/month.
- Nerdster — custom governed workflow pilots from £3,000 + VAT.
- Beyond Arc — production workflow £1,500; AI calls/messages from £149.99/month.
- Flotek / Voco and similar providers demonstrate demand for managed AI reception / front-office automation.

This is competitive research, not a licence to copy protected branding, copy, code or confidential methods. Hay Digital should use legitimate public patterns, permissively licensed tools and original implementation.

## Hay Digital position

Primary promise:

> We automate one piece of repetitive business admin, connect it to the tools you already use, keep you in control of important decisions, and prove whether it saves time or improves outcomes.

Do not lead with:
- multi-agent teams;
- autonomous employees;
- model names;
- technical architecture.

Lead with the business problem.

## Initial customer profile

Start where Haymaker already has a natural route to customers:

- trades and home services;
- local service businesses;
- care / support providers;
- hospitality;
- small professional-services firms;
- owner-managed businesses where missed enquiries, repeated admin or manual follow-up are visible problems.

Do not broaden to enterprise programmes before small-business delivery is repeatable.

## Initial offer ladder — internal pricing hypotheses

Do not publish these yet.

### 1. Free workflow fit call
30 minutes.

Outcome:
- identify one painful recurring process;
- confirm existing tools;
- estimate frequency, owner-hours and commercial impact;
- decide whether automation is worth building.

No speculative "AI transformation" report.

### 2. Single Workflow Pilot
Internal test price range: £595–£995 for simple builds.

Examples:
- enquiry form -> qualification -> acknowledgement -> owner summary;
- missed-call / web-chat lead capture;
- recurring inbox classification and response drafting;
- quote-follow-up workflow;
- document extraction -> structured record -> human approval;
- appointment / reminder workflow.

Fixed written scope. Client owns the underlying accounts where practical.

### 3. Bespoke workflow/system
Internal test starting point: £1,500+ where several systems, custom interfaces, migration or more complex governance are required.

Quote only after process mapping.

### 4. Optional Automation Care
Internal test range: £79–£199/month for small systems.

Includes:
- health checks;
- API / credential-expiry monitoring where supported;
- limited fixes;
- small prompt/rule improvements;
- monthly usage/cost summary;
- escalation for material changes.

Usage charges from external providers should be transparent and preferably remain on the client's own account.

## First productised demonstrator

### Enquiry-to-Action System

Purpose:
Turn an incoming website/email enquiry into a structured, fast owner workflow without removing human control.

Example flow:

1. Enquiry arrives.
2. System extracts:
   - customer/contact details;
   - requested service;
   - location;
   - urgency;
   - key constraints;
   - missing information.
3. Classify the enquiry.
4. Draft an acknowledgement / clarifying reply.
5. Create an owner summary with recommended next action.
6. Human approves any outbound response initially.
7. Record status and follow-up date.
8. If no reply / quote response, prepare follow-up at agreed interval.
9. Track:
   - response time;
   - enquiries processed;
   - follow-ups completed;
   - manual minutes saved;
   - conversion where known.

This demonstrator naturally extends Haymaker websites and can later incorporate the AI receptionist concept.

## Delivery standard

Every Hay Digital workflow should have:

### Written success condition
Examples:
- reduce first-response time from X to Y;
- remove Z minutes of weekly re-keying;
- capture 95%+ of required enquiry fields;
- eliminate missed follow-up tasks.

### Data map
Record:
- what data enters;
- where it is processed;
- what is retained;
- who can access it;
- what leaves the client's systems.

### Permission map
Each agent/tool receives the minimum permissions required.

### Human approval map
Human approval required before high-impact actions such as:
- sending consequential customer communications during pilot;
- creating/refunding payments;
- deleting records;
- changing production configuration;
- placing orders;
- publishing externally;
- making legal, financial, employment or safety decisions.

### Failure path
The workflow must fail safely:
- stop;
- preserve useful state;
- notify a person;
- never invent completion.

### Cost boundary
Set usage limits and alerts before production.

### Test pack
Use:
- normal cases;
- malformed inputs;
- missing information;
- contradictory inputs;
- prompt-injection / hostile text where relevant;
- provider/API failure;
- duplicate events;
- timeout / retry cases.

### Acceptance
Client signs off the narrow workflow before it is expanded.

## Technical approach

Use the smallest reliable architecture.

Preference order:

1. Existing SaaS/native automation capability.
2. Deterministic code / rules.
3. One focused agent with tools.
4. Multiple agents only where separation of responsibility materially improves reliability, review or context management.

For agentic workflows:
- structured outputs between stages;
- guardrails on untrusted input;
- human approval before sensitive side effects;
- resumable state for paused approvals;
- tracing / audit evidence;
- evaluations on representative tasks;
- independent verification for important workflows.

OpenAI's current Agents SDK supports tool use, handoffs, guardrails, resumable state and human-review interruptions. Use those facilities rather than inventing a bespoke agent framework unless a client need requires it.

## Security / compliance baseline

Before a client production release:

- UK GDPR data minimisation;
- clear controller/processor roles;
- DPA where appropriate;
- client data not used to train public models unless explicitly lawful and agreed;
- secrets stored outside code;
- no secrets in logs;
- least-privilege API permissions;
- MFA where supported;
- retention/deletion policy;
- incident and rollback path;
- documented sub-processors/providers;
- explicit human responsibility for consequential outputs.

Seek qualified legal / data-protection advice when the workflow handles high-risk or special-category data or enters regulated areas.

## Sales rule

Do not build a large custom system for a prospect without commercial evidence.

Sequence:

fit call -> narrow paid pilot -> measured result -> optional expansion / care.

If the pilot cannot identify a measurable business benefit, do not force AI into the workflow.

## Internal case study

Use Hay Digital itself as the first safe test environment.

Build a synthetic-first Enquiry-to-Action pilot that can:

- parse a fictional inbound enquiry;
- classify it;
- create a structured brief;
- draft a reply;
- identify missing information;
- route high-risk or ambiguous cases to a person;
- produce trace/test evidence.

Only after this passes should live email integration be considered.

No live customer email, deployment, paid API expansion or new subscription is authorised by this brief.

## Completion criteria for phase 1

Phase 1 is complete when Hay Digital has:

- one documented productised workflow offer;
- one reusable technical workflow template;
- one synthetic demonstrator with tests;
- one independent QA review;
- a simple cost model;
- a data/permission/approval checklist;
- a delivery checklist from fit call to handover;
- a concise website-ready description held internally pending BISE authorisation.

## Sources reviewed

- OpenAI Agents SDK / guardrails and human review:
  https://developers.openai.com/api/docs/guides/agents/sdk
  https://developers.openai.com/api/docs/guides/agents/guardrails-approvals
- Augustova:
  https://www.augustova.co.uk/ai-for-small-business
- Praxen AI:
  https://praxenai.com/services/ai-automation
- ZTech:
  https://www.ztechinc.co/ai-automation
- Nerdster:
  https://nerdster.ai/ai-agents/start
- Beyond Arc:
  https://beyondarc.co.uk/
