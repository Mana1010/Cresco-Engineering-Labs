# Task 9: Implement Frappe UI to Tools Registry Table: Questions

Task 9 is implemented in `frontend/src/portal/tools_registry/CalculationTable.vue`. Please confirm or correct the points below (with Ton where needed).

1. **Look.** I followed the Task 8 decision and kept the Cresco table design, built from frappe-ui's `List`, `ListHeader`, `ListHeaderCell`, `ListRows`, `ListRow` and `ListCell`. At desktop width it's visually identical to the old `<table>`: same row heights (56px), header (34px) and columns within about 1px. Screenshots are in `reports/frappe_ui_fit/tools-registry-table-original.png` and `tools-registry-table-frappe-ui.png`. Is keeping the Cresco look right here too, or should the table use frappe-ui's own style?

2. **Column widths at narrow screens.** The old `<table>` sized its columns from the content. frappe-ui's List is a grid with fixed column tracks (the name and "Approved by" columns share the remaining width). At desktop width they match. Below about 1000px, where the table scrolls sideways at its 760px minimum, some cells wrap differently than before (e.g. "Civil / Stormwater" stays on one line). Is that acceptable?

3. **Paging (outside this task, but related).** The registry still loads 15 rows at a time and loads more on scroll. The 2026-10-20 meeting asked for standard pagination (first/prev/next/last, rows per page), not infinite scroll. frappe-ui's List has no pagination control, so it would be a separate component. Should that be its own task?

4. **"Muted" text colour (carried over).** In the old table, the Category, Version, Approved by and chevron cells were meant to be grey (`--portal-muted`) but rendered dark, because a cell rule overrode them. I kept them dark so the look didn't change. Should they be grey?

**Findings for the frappe-ui assessment**

- **Fits:** the structure (header and rows share one column template; `role="table"` / `row` / `cell` for screen readers), clickable rows (a row with a click listener becomes a real `<button>`, so Enter, Space and focus work without extra code), stable row keys (`row-key="id"`), and the spacing variables (`--list-gap`, `--list-row-padding-x`). Available for later: sortable headers (`ListHeaderCellSort`), checkbox selection and virtual scrolling for long lists.
- **Needed overrides:** header colour and size, light-blue hover, square rows (frappe-ui rounds them), font weight and letter-spacing, and the row lines. frappe-ui's dividers only span the columns and hide around a hovered row, so they're turned off (`divider="none"`) and each row draws an edge-to-edge top line like the old table. About 70 lines of CSS, using the documented `data-slot` hooks.
- **Limits:** no content-based column sizing (tracks are fixed), no built-in pagination, and no horizontal-scroll handling (the card wrapper still does that).
