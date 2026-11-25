# Digest: Engineering Labs Backlog Review (11 Nov 2026)

**Source:** `guide_imgs/CRESCO Engineering Labs _ Scope, Staff, Schedule 20261026 (1).html`. It's marked "DRAFT — NOT YET FINAL" and replaces the 24 Oct version (see `backlog-digest-2026-10-24.md`).

## What changed since 24 Oct

| | 24 Oct | 11 Nov |
|---|---|---|
| Items | 77 in 6 groups | **36 in 5 modules** |
| Estimates and releases | 823 h; R1/R2/R3 | **None.** Estimates, owners, dates and releases aren't filled in yet. |
| Approach | Portal integrates each of the 7 tools itself | Portal = **"container" + 3 generic "sockets"** + docs and a dummy app, so tools can be plugged in later by others |
| Tool-specific work (Env Calc migration, CheckWind/SkyCiv adapters, per-tool PDFs, Arch Extract/Biax) | Itemised | **Removed** as items. The tools remain only as the "portfolio" that sockets must support. |
| Frappe | Not mentioned (Laravel-style wording) | **Explicit:** Frappe v16 container, Frappe whitelisted middleware, DocTypes, Desk, Web Forms, Jinja2 print formats, `deploy-frappe-app.sh` |
| Excel runner | POC mock-up only | **In scope:** Socket 2, MS Excel tool (#13, #17), sourced from "STAFF Chat" |
| Approval states | POC only | In the tool registry data model (#26) |

## The 36 items

**M01 Portal Container & Service Chassis (11)**
- 01 Design: To-Be container architecture (standalone Frappe v16, DB isolation, peer-service routing)
- 02 Design: DB schema (**still says PostgreSQL, `cresco_eng_`, UUID**)
- 03 Design: API security (X-API-Key, rate limit, M365 Entra SSO)
- 04 Design: Standard response envelope `{status, source, calculation_id, cached_at, standard_edition, data, errors}`
- 05 Develop: Infrastructure (DO SYD1, PostgreSQL, Redis, Nginx, GitHub Actions)
- 06 Develop: Tables and migrations (`cresco_eng_`, UUID, FKs)
- 07 Develop: X-API-Key middleware (**"Frappe whitelisted middleware"**)
- 08 Develop: Immutable calculation audit log (`cresco_eng_calculation_log`)
- 09 Develop: `/api/v1/health` endpoint
- 10 Deploy: Staging deployment (`deploy-frappe-app.sh`)
- 11 Deploy: Production cutover

**M02 Integration Sockets & Contracts (9)**
- 12 Design: Socket 1, Frappe Native contract (`/api/v1/socket/frappe-native`, internal Python service classes, per the Tool Template)
- 13 Design: Socket 2, MS Excel contract (`/api/v1/socket/excel-tool`: input cell mapping, locked formulas, JSON extraction)
- 14 Design: Socket 3, external contract (`/api/v1/socket/external-app`: REST/gRPC, token auth, DTO mapping)
- 15 Design: Retry and circuit breaker (3 attempts 1s/2s/4s; Redis cache 24 h CheckWind / 25 min SkyCiv)
- 16 Develop: Socket 1 controller (whitelisted methods, validation, result formatting)
- 17 Develop: Socket 2 **workbook evaluator (openpyxl)**, cell-range parser, result extractor
- 18 Develop: Socket 3 generic external adapter (OAuth2/API key, retry, Redis cache)
- 19 Develop: Universal socket router and transformer
- 20 Deploy: Socket endpoint verification

**M03 Dynamic Documentation & Dummy App (5)**: lets tool owners self-integrate
- 21 Design: Interactive socket docs (Swagger UI / OpenAPI 3.0)
- 22 Design: Dummy app test-suite spec (payloads and benchmarks for all 3 sockets)
- 23 Develop: Swagger UI page embedded in **Frappe Desk**, with live payload tester
- 24 Develop: Dummy app throughput tester (fires payloads through all 3 sockets)
- 25 Deploy: Publish docs and sign-off

**M04 Tool Registry & Staff Workbench (7)**
- 26 Design: Tool registry **DocType** schema (registration, socket assignment, version routing, approval states)
- 27 Design: Staff workbench and report UI architecture ("**server-side rendered** forms", JSON viewer, PDF, history wireframes)
- 28 Develop: Tool catalogue management UI (**Frappe Desk DocType + Web Forms**)
- 29 Develop: Staff workbench shell and nav (M365 SSO guard, tool menu, input form builder, history viewer)
- 30 Develop: Dual output and **Jinja2 print-format** PDF with "Preliminary" watermark
- 31 Develop: Usage analytics dashboard (unique users, volume, popularity, API health, quota)
- 32 Deploy: Staff workbench UAT sign-off

**M05 Governance, QA & Handover (4)**
- 33 Design: Disclaimer, branding, 7-year retention
- 34 Deploy: UAT and socket pipeline verification
- 35 Deploy: 1-week hypercare
- 36 Deploy: 30-day warranty and handover (ADRs)

## Things to flag

1. **Frappe confirmed, but the DB conventions are still contradictory.** #02, #05 and #06 say PostgreSQL / `cresco_eng_` / UUID / migration scripts, while #26 says DocType schema and #01's notes say MariaDB. Frappe DocTypes create `tab<Name>` tables through `bench migrate`. → Ask Ton (he owns the schema, meeting on 16 Nov).
2. **openpyxl can't calculate Excel formulas.** It only reads the values Excel cached at the last save. A server-side evaluator (#17) needs a formula engine (e.g. the `formulas` or `pycel` Python libraries, or headless LibreOffice). → Raise early.
3. **The workbench UI approach is unclear.** #27 says "server-side rendered forms" and #28 says Desk + Web Forms. Our current portal is a Vue/frappe-ui SPA. → Confirm whether the staff workbench is the Vue frontend, Web Forms, or Desk.
4. **UAT items (#32, #34) conflict with the group message** ("there will be no UAT; dev-complete codebase handed to Other Projects contractor").
5. **Socket 3 says REST/gRPC.** gRPC is unusual in Frappe; likely just REST in practice.
6. **The working integration notes are still AI noise.** They mention PLM systems, lab instrumentation, IoT and Kafka-style brokers; "Engineering Labs" was read as a physical laboratory. Ignore them.
7. **POC mock-ups (projects, automations, KPIs, revisions) are still "not confirmed scope".** Only the catalogue approval states made it in (#26).
8. **Tristan's role ("container" + "sockets")** = M01 + M02, probably M03 too. Ton does design/scaffolding; Jerome does DevOps (#05, #10, #11, #35).
