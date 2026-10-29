# Meeting notes — checkpoint after 2026-10-20 (Ton / Tristan)

Reference copy as shared by Tristan; the exact meeting date wasn't included in the notes. Next sync: 2026-10-27.

## Summary
- **Primary objective:** assess whether **Frappe UI** components can meet the UI/UX design requirements of the Cresco Engineering Labs Portal (POC).
- Tristan showed progress:
  - a breakdown of Frappe UI elements (sidebar menus, metric cards, pills/buttons, Tools Registry views);
  - DocTypes from the POC (labs_metric, portal_stat, portal_event, …) and fixtures.
- **Schema isn't final.** Open question: should labs_metric be stored by background scheduled jobs, or should metrics be calculated on the fly?
- **Data fetching:** Tristan proposed VueUse `useFetch`. Ton strictly prohibited anything that bypasses the Frappe ORM or permission system, because of data-leak risk.
- **Naming:** "Engineering Labs", "Engineering Portal" and "Engineering Labs Portal" are the same application.
- **Hybrid approach:**
  - Tristan may hand-code designated modules, e.g. the **Tools Registry**, for learning and ownership.
  - AI is used for speed on the other parts.
- Ton congratulated Tristan on moving from intern to regular employee. Quarterly focus areas: communication/soft skills, and attention to detail.

## Decisions
1. Write a comprehensive **UI gap analysis report**: every Cresco design element compared with Frappe UI components, noting which need external CSS libraries or custom components.
2. **Bypassing the Frappe ORM for data fetching is prohibited.** `useFetch` may not be used unless Tristan empirically proves it enforces Frappe user permissions and ORM security.
3. **Hybrid development:** AI for complex parts; Tristan may hand-code selected backlog modules, such as the Tools Registry.

## Action items
| Task | Owner | Due | Notes |
|---|---|---|---|
| UI inventory report: Cresco design elements vs Frappe UI out-of-the-box components | Tristan | 2026-10-27 | Element breakdown, availability (yes/no), recommendations (CSS / external libraries) |
| Test whether `useFetch` respects Frappe ORM permissions | Tristan | 2026-10-27 | Use a test user without access to the Employee table and verify access control |
| Finalize the schema; decide background jobs vs on-the-fly calculation | Ton & Tristan | Unspecified | Review once Labs portal development starts |
| Set up the next sync meeting | Ton | 2026-10-27 | Review the Frappe UI inventory report |
