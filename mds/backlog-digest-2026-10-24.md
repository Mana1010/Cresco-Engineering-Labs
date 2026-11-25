# Digest: Engineering Labs Backlog & Release Plan (24 Oct 2026)

**Source:** `guide_imgs/CRESCO Engineering Labs _ Scope, Staff, Schedule 20261026 (1).html`, marked **"DRAFT — NOT YET FINAL"**. It's a planning view, not a committed baseline.

## 1. The big picture

- **What the portal is:** a **"Program / Tool Manager"** for Engineering Labs. It's one portal that registers engineering tools, controls who can use them, connects to them, shows their results and reports, and keeps history, audit and health records.
- **Scope boundary:** the portal does **not** own the engineering logic. Formulas, standards, solvers, reference data and numerical correctness stay with each tool's owner. The portal owns registration, access, interface contracts, data exchange, results, reports and operational control.
- **Size:**
  - 77 backlog items, **823 h** estimated.
  - Capacity is **1.0 + 0.5 FTE = 60 h/week**.
  - Indicative timeline is **14.8 weeks**: 11.8 weeks of work plus three reserved one-week deployment windows.
  - The plan makes no allowance for leave, meetings, review delays or rework.

## 2. The seven tools

| Family | Tool | Portal interaction |
|---|---|---|
| Internal | Environmental Calculator | Register / connect (migrate legacy client-side HTML tool to a server-side service) |
| Internal | Climate Zone | Register / connect (location → classification lookup) |
| Internal | ARR / IFD Stormwater | Register / connect (BOM IFD rainfall + council rules) |
| External API | CheckWind (Revolutio) | API adapter: API key, 24 h Redis cache, 3-attempt retry, attribution ≥10px |
| External API | SkyCiv v3 | API adapter: 25 min session cache, getWindLoads / solveModel / getAnalysisReport |
| Design automation | Arch Extract | Service integration (parse architectural files) |
| Design automation | Biax | Service integration (residential slab/framing drafting; future BIM/Revit DTO) |

## 3. Releases

| Release | Theme | Items | Hours |
|---|---|---|---|
| **R1** | Portal + **Environmental Calculator** | 27 | 227 |
| **R2** | Portal expansion + Climate Zone, ARR, **CheckWind, SkyCiv**, history, dashboard | 39 | 394 |
| **R3** | **Arch Extract + Biax**, production cutover, hypercare, warranty | 11 | 202 |

## 4. Six scope groups

| Group | Items | Hours |
|---|---|---|
| 01 Foundation & Program/Tool Management | 23 | 216 |
| 02 Internal Tool Registration & Integration | 12 | 111 |
| 03 Tool Outputs & Reporting (PDF) | 14 | 121 |
| 04 Staff Program/Tool Manager Interface | 10 | 98 |
| 05 External Tool Integrations | 11 | 121 |
| 06 Arch Extract & Biax | 7 | 156 |

## 5. The staff UI items (group 04: the frontend work)

| # | Item | Release | Hours | What it means |
|---|---|---|---|---|
| 18 | Program/Tool Manager UX | R1 | 6 | Wireframes: tool selection, input forms, JSON output viewer, PDF download, history table |
| 19 | Staff SSO contract | R1 | 6 | Microsoft Entra ID OAuth 2.0 / OIDC standard |
| 50 | Shell & navigation | R1 | 12 | Layout, navigation, responsive CSS, **SSO login guard** |
| 51 | Tool access & input controls | R1 | 12 | Validated input form per tool, matching each API's request schema |
| 52 | Result view & download | R1 | 9 | Formatted JSON result panel + one-click PDF download |
| 20 | Usage & health metrics spec | R2 | 6 | Unique users, API quota, calc volume, tool popularity, API health |
| 53 | Activity & output history | R2 | 15 | History table from the calculation log for the logged-in user, PDF re-download |
| 54 | Usage & health dashboard | R2 | 18 | The metrics above as a live dashboard |
| 72 | User enablement | R2 | 8 | Train-the-trainer sessions |
| 73 | Staff portal acceptance | R2 | 6 | UAT sign-off: forms, SSO, history, PDF |

## 6. Concrete technical commitments in the source descriptions

- **Hosting:** DigitalOcean Sydney (SYD1), **managed PostgreSQL**, Redis, Nginx, GitHub Actions CI/CD (#27).
- **Database:** `cresco_eng_` table prefix, **UUID primary keys** (#2, #28).
- **API:**
  - `/api/v1/…` routes (#6).
  - `X-API-Key` header auth with rate limiting (#3, #29).
  - A standard JSON envelope `{status, source, calculation_id, cached_at, standard_edition, data, errors}` (#5, #31).
  - Errors mapped to 401 / 422 / 502 / 503 / 504 (#7, #33).
  - A `/api/v1/health` endpoint (#34).
  - OpenAPI 3.0 / Swagger (#36).
- **Endpoints named:**
  - `POST /api/v1/environmental-calc`
  - `GET /api/v1/climate-zone`
  - `POST /api/v1/arr-stormwater`
  - `POST /api/v1/wind-assessment`
  - `POST /api/v1/structural-analysis`
  - `POST /api/v1/wind-loads`
  - `POST /api/v1/arch-extract-biax`
  - `GET /api/v1/calculations/{id}/pdf`
- **Audit:** an append-only `cresco_eng_calculation_log` with request/response payloads, `execution_ms`, status, `requested_by` and `project_ref`, kept **7 years for PI insurance** (#4, #30).
- **Background jobs:** Redis named queues `cresco_sync`, `cresco_ai` and `cresco_notifications` with RQ workers (#35).
- **Wind standards:** AS/NZS 1170.2 **2011 vs 2021** routing, defaulting to 2021 (#6, #32).
- **IP protection:** proprietary formulas, coefficients and lookup tables stay server-side and never appear in API JSON or JavaScript (#12).
- **PDF:** server-side HTML/CSS → PDF engine (#42), branded per the Corporate Identity Manual 2025 (#15), with a mandatory **"Preliminary — Subject to Engineer Review"** watermark and disclaimer (#16), and one template per tool (#43–#48).

## 7. Things to flag (my review)

1. **The backlog wasn't written for Frappe.** The source descriptions describe a standalone REST service: `App\Adapters\CheckWindAdapter` (a PHP/Laravel-style namespace), "middleware", a "dependency injection container", "server-side rendered page layouts", `X-API-Key`, a `cresco_eng_` prefix and UUID keys. The implementation plan says **Frappe v16**, and Frappe already provides much of this differently:

   | Backlog | Frappe equivalent |
   |---|---|
   | `X-API-Key` header | `Authorization: token key:secret` |
   | `/api/v1/...` routes | `/api/method/...` and `/api/v2/...` |
   | `cresco_eng_` tables | `tab<DocType>` tables |
   | Error middleware | Built-in exception → HTTP mapping |
   | Redis named queues | RQ queues (named queues are supported) |
   | PDF engine | Print formats / PDF generation |
   | M365 SSO | Social Login Keys (Office 365 provider) |

   → **Ask Ton:** should the backlog's API and DB conventions be followed literally, or mapped to Frappe equivalents?

2. **The database:** the backlog says managed PostgreSQL. `cresco.local` currently runs **MariaDB**. This was already asked in `questions/task-7.md` (Q7).

3. **No Excel / protected-workbook runner in the backlog.** Excel appears only in POC mock-up E ("concept, not confirmed scope"). The backlog's internal tools are Environmental, Climate Zone and ARR, migrated to **Python service classes**. → Hold off on the Excel preview / Jspreadsheet work until it's confirmed.

4. **Several features we've built are POC concepts, not backlog items.** The document says POC mock-ups are "a discussion aid… not a confirmed scope baseline". These are **not** in the 77 items:
   - catalogue approval workflow (approve / deprecate / re-approve);
   - revisions and returns;
   - automations;
   - the Portal ↔ Labs project provisioning view;
   - the projects workspace;
   - Labs Home KPIs such as first-time pass, consistency flags and coverage ("No KPI values are asserted").

   The backlog's dashboard (#20, #54) is **usage and API health only**: unique users, quota, volume, tool popularity, API health.

5. **Dependency order looks off.** R1 includes the result view + PDF download (#52), but the PDF download endpoint (#49), the calculation log (#30) and the audit spec (#4) are in **R2**. R1's download would need either an interim approach or those items moved earlier.

6. **The "working integration notes" are noise.** They're the auto-generated-looking long paragraphs, and they propose tech that contradicts the stated stack: Kubernetes, Kafka, Airflow, GraphQL, SOAP, SFTP/PGP, Prometheus/Grafana. #73 even misreads "staff form submissions" as a separate form system. The document says they're "subject to clarification", so treat them as unverified.

7. **Tool access mode per tool is still open** (clarification theme 1): launch/link vs embedded vs API, and whether staff run tools directly from the portal. This decides what "Tools Registry" and the "runner" screens must do.

## 8. Clarification themes the document lists (for Ton / CRESCO)

1. Tool access model per tool.
2. Interface and environment readiness: APIs, versions, test environments, credentials, rate limits, sample requests/responses.
3. Inputs, outputs and reporting: native tool reports vs portal-rendered, file retention.
4. Ownership and support boundary after go-live.
5. Acceptance: portal UAT kept separate from engineering-accuracy sign-off.
6. Security, audit and operations: roles, credentials, retention, monitoring.

## 9. CRESCO inputs needed

- M365 Entra tenant/app setup and test users.
- CheckWind and SkyCiv credentials and quotas.
- Working versions and interface docs for the internal tools.
- Arch Extract / Biax access and sample files.
- Approved reference datasets.
- Brand assets, report samples and disclaimers.
- Environment details (DNS, secrets route).
- Named tool owners, UAT contacts and sign-off contacts.
