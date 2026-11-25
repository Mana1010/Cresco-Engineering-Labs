# Review: Cresco Engineering Portal, Developer Brief v1.0

**Source:** `references/Cresco_Labs_Developer_Brief_v1_0 (2).pdf` (23 pages)
- Reference CRESCO-ENG-PORTAL-DEV-BRIEF-V1.0, dated **8 April 2026**.
- Author: Isaac Mannion (Programme Owner). Director: Shane Lutze. Consulted: Vince Chaffey (Engineering Manager).

## 1. Where it sits among our documents

| Document | Date | Role |
|---|---|---|
| **Developer Brief v1.0** | 8 Apr 2026 | The **original client requirements**, written for one external contractor on Laravel |
| POC v0.7 (`references/Cresco_Engineering_Labs_POC_v0_7.html`) | ~Oct 2026 | Concept mock-ups (projects, automations, Excel, KPIs). Not confirmed scope. |
| Backlog Review | 11 Nov 2026 | Servio's **reinterpretation** of the brief for Frappe, as "container + 3 sockets" + docs, with the Excel socket added from "STAFF Chat" |

Treat the brief as the **source of the requirements** (what CRESCO needs and why). Treat the 11 Nov backlog as **how our team plans to deliver it**. Where they disagree, ask Ton.

## 2. What the brief settles

| Open question | Brief's answer | Section |
|---|---|---|
| Separate service or part of Portal? | **Standalone peer service**: own codebase, deployment and database. Not a module in the Platform. | §1, §1.2, §2.2 |
| Separate login for staff? | **Yes, its own SSO login**, using the same Entra ID identity provider as the Platform. "No separate user registration." CRESCO provides the Entra app registration. | §4.5, §8.2 |
| Who calls the API? | Exactly one consumer at launch: the **Cresco Platform**, via a static `X-API-Key` header. Future: Auth0 M2M tokens (documented, not built). The middleware should be a "replaceable guard". | §8.2 |
| Who can access the staff UI? | **Only authenticated CRESCO staff**; no client access. No roles or permission levels are defined. | §4.5 |
| Does it touch projects? | **No.** It doesn't interact with Total Synergy, doesn't manage project lifecycle, and isn't part of the QA chain. It only receives an optional `project_ref` and returns a `calculation_id`. | §1, §1.3 |
| What menus? | Staff UI is "intentionally minimal… **not a dashboard, not a project management tool**". Features: tool selection → input form → JSON results → PDF download; **calculation history**; **metrics view**. | §4.5 |
| Do internal tools exist? | **Yes, as client-side HTML/JS** (Environmental Calc, Climate Zone, ARR). Logic must be moved server-side; the HTML front-ends are not migrated. | §5 |
| Can we start? | "**No development work should begin until all Phase 1 items are delivered**": spec packs with benchmark tests, GitHub repo, database and hosting. | §10 |

## 3. Conflicts with our current direction

| Topic | Brief (Apr) | 11 Nov backlog / current setup | Note |
|---|---|---|---|
| Framework | "Same as Cresco Portal (**currently Laravel 11, PHP 8.3**)" | Frappe v16 | The *rule* is "match the Portal's framework". If Portal Core is now Frappe (`portal_core`), the rule itself justifies Frappe. The Laravel specifics are outdated. |
| Database | **Azure SQL Database**, `cresco_eng_` prefix | Backlog: DigitalOcean PostgreSQL. Local: MariaDB. | Three different databases across documents. Ask Ton (Nov 16). |
| Hosting | **Azure App Service**, separate resource group | DigitalOcean SYD1 | Ask Jerome or Ton. |
| Staff UI | **Server-side rendered pages, not a SPA** | Our portal is a Vue/frappe-ui SPA | Frappe equivalents: `www/` Jinja pages or Web Forms. Ask Ton whether the Vue SPA is acceptable. |
| Relationship to Portal | Separate deployment and database | Ton (20 Oct): `portal_core` is a mandatory prerequisite; users and permissions come from Portal Core | A direct conflict. Same site or separate deployment? |
| Excel tools | **Not mentioned at all** | Socket 2, MS Excel (#13, #17), from "STAFF Chat" | Came later from staff conversations. Confirm it's really required. |
| "Sockets" | Not used. The brief has a service layer + an **adapter pattern** (common interface). | 3 sockets + universal router | The same idea under new names: Socket 1 = internal service classes, Socket 3 = adapters. |
| Timeline | **16 weeks + 4-week buffer** (20 weeks), 3 phases with gates | 9 Nov – 18 Dec (6 weeks), handover to the "Other Projects" contractor | Explains why the backlog was cut to a reusable framework. |
| PDF | DomPDF / Browsershot (PHP libraries) | Jinja2 print formats | Frappe equivalent is fine. |
| UAT / sign-off | Phase gates signed off by Isaac Mannion | Group message: "no UAT" | Ask who signs off now. |

## 4. Gaps and inconsistencies inside the brief

1. **The ARR tool is incomplete.** §5.3 exists but isn't in the contents, has **no endpoint** in §8.1 and **no PDF template** in §7.2, and isn't in the Phase 1 tasks (§9.2), yet its spec is "required before Phase 1" (§10 #3). The backlog later added `/api/v1/arr-stormwater`.
2. **§13 says "the initial four" tools,** but the brief describes six or seven.
3. **The JSON classification field is missing.** §11.1 requires "Preliminary — Subject to Engineer Review" as **metadata in every JSON response**, but the §4.2 envelope has no field for it. Suggest adding e.g. `"classification": "preliminary"`.
4. **"Not a dashboard" vs. a required metrics view** (§4.5). These are compatible but read as contradictory; the metrics view is required.
5. **Google Maps Geocoding** is listed as an integration (§3.2) but appears nowhere else. It's probably for turning an address into lat/lng for CheckWind and Climate Zone. The 11 Nov backlog doesn't mention it.
6. **Page 19 is blank** (likely a lost diagram or table).
7. **§1.3 promises a diagram** ("The following diagram illustrates…"), but it's a table.

## 5. Details worth keeping for the build

- **Response envelope (§4.2).** `status` is `success | partial | error`:
  - `partial` = some data returned with warnings, e.g. one wind direction failed.
  - `error` = the request failed entirely.
  - `cached_at` is set only when the result is served from cache.
- **Audit log fields (§4.3):** `id` (UUID), `tool`, `api_version`, `request_payload`, `response_payload`, `status`, `execution_ms`, `requested_by` (API key ID or user), `project_ref` (nullable), `created_at`.
  - The log is append-only and kept for **at least 7 years**.
  - Used for PI defence, API cost tracking, performance and debugging.
- **Standards versioning (§4.4):** every wind endpoint takes `standard_edition`, routes to the 2011 or 2021 Hazard API endpoint, defaults to 2021, and includes the edition in the JSON and the PDF.
- **Metrics view (§4.5).** Six metrics:
  - unique users (daily/weekly/monthly);
  - API quota, including renewal dates;
  - calculation volume with trends;
  - tool popularity;
  - external API health over 24 h (connectivity, average response time, error rate);
  - **PDFs generated and storage used.** The 11 Nov backlog #31 dropped this one.
- **Health endpoint (§8.1):** "uptime, **API connectivity status**". So it should include CheckWind/SkyCiv reachability, not just DB and Redis.
- **CheckWind (§6.1):**
  - attribution: at least 10px text or a 120px logo;
  - **non-compete clause** needs legal review;
  - fallback is SkyCiv `standalone.loads`;
  - cache by (lat, lng, height, edition) for 24 h;
  - errors map to 503 (quota), 422 (invalid location) and 502 (server error).
- **SkyCiv (§6.2):**
  - credentials go in the JSON **body**, not headers;
  - cache the session for 25 minutes (it expires after 30);
  - on session expiry, re-authenticate and retry;
  - errors map to 401, 422 and 504;
  - internal use is OK; charging external customers needs a commercial agreement.
- **Wind data governance (§6.4):** CheckWind and SkyCiv give **different** wind results for the same site, so CRESCO must decide the workflow before both are exposed.
- **Final handover deliverables (§12.2):**
  - ADRs (Architecture Decision Records);
  - code docs for the calculation services;
  - OpenAPI 3.0 spec;
  - deployment runbook;
  - data seeding procedure;
  - adapter update procedure;
  - a handover session.
- **Code quality (§12.3):**
  - business logic in services, never in controllers;
  - unit tests with benchmark cases;
  - adapter tests against mocks;
  - a linter;
  - no hard-coded credentials.

## 6. Laravel → Frappe translation (for reading the brief)

| Brief (Laravel) | Frappe v16 |
|---|---|
| Controllers (thin) | `@frappe.whitelist()` methods |
| Service classes | Plain Python modules/classes in the app |
| `App\Adapters\CheckWindAdapter` + DI container | A Python adapter class + a registry or factory (Frappe has no DI container) |
| Middleware | `before_request` hook / a decorator |
| Migrations, `cresco_eng_` tables, UUID PK | DocTypes + `bench migrate` (`tab<DocType>` tables) |
| `.env` | `site_config.json` / Password fields |
| Queue workers | `frappe.enqueue` + RQ workers |
| DomPDF / Browsershot | Print Formats + `frappe.get_pdf` |
| PHP CS Fixer | `ruff` / pre-commit (Frappe's standard) |
| PHPUnit | `FrappeTestCase` / `bench run-tests` |
| Server-side rendered pages | `www/*.html` + `.py` (Jinja) or Web Forms |

## 7. Questions to raise (add to the Nov 16 list)

1. The brief says "same framework as the Cresco Portal". Is Portal Core now Frappe, which is why we use Frappe?
2. The brief says separate codebase, database and deployment, but `portal_core` was described as a required dependency. Which applies?
3. Database and hosting: Azure SQL + Azure App Service (brief), DigitalOcean + PostgreSQL (backlog), or MariaDB (Frappe default)?
4. Staff UI: the brief requires server-side rendered pages, not a SPA. Is our Vue/frappe-ui frontend acceptable?
5. Have the §10 Phase 1 items been delivered (the Environmental Calculator, Climate Zone and ARR specs with benchmark test cases)?
6. The Excel socket isn't in the brief. Who requested it ("STAFF Chat"), and which Excel tools need it?
7. Who signs off now: Isaac Mannion phase gates as in the brief, or none (group message: no UAT)?
