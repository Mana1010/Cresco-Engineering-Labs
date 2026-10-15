# Task 2: Engineering Labs > Home UI: Questions

Task 2 is implemented. Where the plan was open, I used the defaults below. Please confirm or correct them.

1. **Calculation Catalogue and Tools Registry pages.** No mockups were provided for these. Both routes exist (`/engineering-labs/calculation-catalogue`, `/engineering-labs/tools-registry`) so the submenu can navigate and highlight, but each page only shows a "This page hasn't been built yet" card. Is that fine for now?
2. **Dashboard highlight.** Now that there are real routes, "Dashboard" is highlighted only on `/portal`. On Engineering Labs pages only the active submenu item is highlighted, so two items are never highlighted at once. Is that what you want?
3. **Getting back to the Dashboard.** Dashboard is still static (Task 1), so once you're in Engineering Labs the only way back to `/portal` is the browser's back button or the address bar. Should Dashboard become clickable?
4. **Mockup 2 page header.** I removed the "Metrics & Usage" title and the paragraph under it, as instructed. I also left out mockup 2's own top bar (breadcrumb "Engineering Labs / Metrics", the "Management" badge, and "Isaac Mannion / Growth & Innovation Manager"), because the portal header from mockup 4 stays in its place. Do you want the breadcrumb or the role badge added to the portal header?
5. **Colours.** The bar charts and the "Time to first calc" value use Cresco blue (`#00a0e3`) instead of the purple in mockups 2 and 3, to match the portal. Green, orange and red are kept for pass, warning and return states. Is that right?
6. **Demo data.** All figures are the demo values from the mockups, kept in `public/js/portal/engineering_labs/homeData.js`. Where should real data come from later, such as new doctypes or the calculation audit log? This can wait until a later task.
7. **Timeliness card.** Mockup 2 cuts off partway through this card. I included the three visible rows. Are there more rows?
8. **`/engineering-labs` with no sub-page.** This redirects to `/engineering-labs/home`, and so does any unknown `/engineering-labs/...` path. Is that OK?
