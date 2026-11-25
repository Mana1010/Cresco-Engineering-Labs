# Schema Meeting Prep (16 Nov 2026)

These are study notes on what the documents *imply*. They aren't a schema design; Ton owns the design.

**Sources:**
- Developer Brief v1.0 (Brief)
- Backlog Review 11 Nov (#)
- Standard Engineering Tool Template (Template)
- Servio Proposal (Proposal)
- STAFF quick chat (Chat)
- Ton's 20 Oct meeting (Ton)

**Decided so far:**
- Frappe v16.
- PostgreSQL.
- Shared Microsoft 365 sign-in with Portal Core.
- Container + 3 sockets (Frappe Native, Excel, External).
- Tools are added by configuration, not code (Chat).

---

## 1. Tables the documents imply

### A. Tool Registry (#26, #28; Template manifest; Chat "add a tool")
The catalogue of tools. Adding a row = adding a tool, with no code change.

| Field | Source |
|---|---|
| tool_id, name, description, category | Template manifest |
| version, contract_version, engine_version | Template manifest |
| socket_type: Frappe Native / MS Excel / External | #26 "socket assignment" |
| Socket 1 config: tool app + method (e.g. `arr_tool.api.tool.calculate_tool`) | Template |
| Socket 2 config: workbook file, input cell map, result cell map, locked formulas | #13 |
| Socket 3 config: base URL, auth type, API key (Password field), cache TTL | #14, #15, Brief §6 |
| status: Draft / Under review / Approved / Deprecated | #26 "approval states", POC Mock-up C |
| approved_by, approved_on | #26, Proposal §9.1 "Logic Gate" |
| attribution text (e.g. "Data provided by Revolutio Hazard API") | Brief §6.1 |
| route, capabilities | Template manifest |

- **Child table, Tool Input:** field key, label, type, unit, required, min/max, options. Needed for #29 "input form builder".
- **Child table, Tool Output:** key, label, unit, highlight?

### B. Calculation Log (#08; Brief §4.3, §11.3): append-only, 7 years
| Field | Source |
|---|---|
| id (UUID) | Brief §4.3 |
| tool (Link → Tool Registry) | Brief §4.3 |
| api_version | Brief §4.3 |
| request_payload (JSON), response_payload (JSON) | Brief §4.3 |
| status: success / partial / error | Brief §4.2–4.3 |
| execution_ms | Brief §4.3 |
| requested_by (user, or API client) | Brief §4.3 |
| project_ref (nullable) | Brief §4.3 |
| created_at | Brief §4.3 |
| run_id, engine/methodology/dataset versions | Template "traceability" |
| cached_at, standard_edition | Brief §4.2 envelope |

- **Frappe:** permissions Create + Read only (no Write/Delete), plus controller checks. Frappe's Version log is NOT a substitute: it tracks edits, not runs.

### C. Calculation Catalog entry / run approval (Ton 20 Oct; POC Mock-ups B, G)
A run submitted with "Add to Project" for approval. **Open question:** is this a separate table, or extra fields on the Calculation Log (the log must stay immutable, so approval probably needs its own record)?
- Possible fields: calculation (Link → Log), project, classification/status (Preliminary / Approved / Returned), reviewer, reviewed_on, notes, PDF file.

### D. API Client (#03, #07)
- name, API key (hashed / Password), active, rate limit, scopes. Brief §8.2: one consumer at launch (Portal Core).
- **Open:** if Labs shares a site with Portal Core, are API keys needed at all? Could use direct Python calls or Frappe's own token instead.

### E. Generated Report / PDF (#30; Brief §4.5 metrics)
- calculation (Link), file, size. Needed for "PDFs generated + storage consumed" metrics.
- Could be just a File attached to the log or run.

### F. External API usage / quota (#18, #31; Brief §4.5)
- provider, quota limit, used, renewal date. Health stats (response time, error rate over 24 h) can probably be computed from the log.

### G. Project data: NOT a Labs table
- Comes from **portal_core** (Ton 20 Oct). Proposal §7.3 "Project Parameter" DocTypes map Portal Core fields (site coordinates, materials) to tool inputs, which is the basis for Project Lookup auto-fill.

### H. Existing POC DocTypes in `engineering_labs`
- Labs Calculation, Labs Metric, Labs Consistency Flag, Labs External API, Cresco Project, Portal Stat, Portal Event, Portal News Post, Portal Team Member.
- **Ask which survive, get replaced (e.g. Cresco Project → portal_core Project), or get dropped.**

---

## 2. Frappe mapping notes

| Topic | Note |
|---|---|
| Table names | Frappe names tables `tab<DocType>`. The `cresco_` / `cresco_eng_` prefix (Brief, Proposal) can only be applied via the DocType *name*, e.g. "Cresco Eng Calculation Log" |
| Primary keys | Brief and Proposal want UUIDs. Check whether v16's UUID naming is available, or use autoname `hash` / `UUID` |
| JSON payloads | JSON field type (PostgreSQL stores it as JSON/JSONB) |
| Secrets | Password fieldtype or `site_config.json`; never in code |
| Permissions | Use `frappe.get_list` (permission-aware), never `get_all` / `db.sql` (Ton) |
| PostgreSQL | Avoid raw SQL; case-sensitive `LIKE`; confirm portal_core is on Postgres too |
| Fixtures | DocTypes + sample data as fixtures for local restore (Ton 20 Oct) |

---

## 3. Questions to raise

**Schema and data**
1. Same Frappe site (and PostgreSQL database) as portal_core? The Compliance doc proposed MariaDB for Portal Core.
2. Naming: `cresco_eng_` prefix and UUID keys (Brief, Proposal), or Frappe's default naming?
3. Approval of **runs**: a separate table from the immutable Calculation Log?
4. Which existing POC DocTypes stay, change, or go?
5. Is `project_ref` a Link to portal_core's Project, or a plain text reference (Brief: nullable string)?

**Contracts**
6. Two envelopes: Template (`success`, `tool`, `results`, `metadata`) for tool → portal, and Brief (`status`, `calculation_id`, `cached_at`, `data`) for portal → Portal Core? Where does the "Preliminary" classification go in JSON (Brief §11.1)?
7. Endpoints: per tool (Brief §8.1) or per socket (#12–14)?
8. Access to the `labs-template` repo and one tool app (e.g. `arr_tool`) to test Socket 1?
9. Who designs the socket contracts and dummy payloads (#12–#14, #22)?

**Approval and menus** (already drafted)
10. History: its own menu, or part of the Calculation Catalog?
11. Portal Core results: immediate (Preliminary) or approved first? Does approval apply to API requests?
12. New tools: approval first? Tools Registry shows only approved tools, and pending ones appear in the Calculation Catalog? Who can add and approve?

**Other**
13. Excel socket: openpyxl can't recalculate formulas. Use the `formulas` library or LibreOffice?
14. My hours: full time on Labs now, or keep the T–Th / MWF split?

---

## 4. During the meeting
- Write down every decision with its date and reason, then copy it to `mds/decisions.md` afterwards (these become the ADRs required at handover, #36).
- If a decision conflicts with a document (Brief, backlog), note which one it overrides.
