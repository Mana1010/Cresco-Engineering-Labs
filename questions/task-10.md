# Task 10: Remove Approved By and Status in Tools Registry

## Done

The **Status** and **Approved by** columns, and their cell data, were removed from the Tools Registry **table view** (`frontend/src/portal/tools_registry/CalculationTable.vue`).

- The table now shows: Calculation, Type, Category, Ver, and the row arrow.
- The Calculation column takes the freed width.
- `vue-tsc` and `vite build` both pass.

## Questions

Status and approval data also appear elsewhere in the Tools Registry. I left these unchanged because the task only says "column":

1. **Card view.** `CalculationCard.vue` (the grid toggle) also shows "Status" and "Approved by". Should they be removed there too, so the card and table views match?

Answer: Yes

2. **Details modal.** `CalculationDetailsModal.vue` (opened by clicking a row) shows a status pill in the header, an "Approved by" field, and the **Deprecate / Re-approve** buttons. Should the status pill and "Approved by" field be removed? Should the approve/deprecate actions stay?

> Yes 3. **Status filter.** `CalculationFilters.vue` has a "Filter by status" dropdown, and the registry **defaults to showing only Approved** calculations (`filters.status = "Approved"` in `ToolsRegistryView.vue`). If status is hidden, should:

- (a) the filter stay, still defaulting to Approved;
- (b) the filter be removed, but the registry still list only Approved calculations; or
- (c) the filter be removed and all statuses listed?

4. **Awaiting approval list and status counts.** The view also shows the "Awaiting approval" list and per-status counts. Are these unaffected by this task?

> if they are commented out then just remove it, the divs itself

5. **"Data" scope.** Does "remove the data" mean only hiding it in the UI, or also dropping `status` / `approved_by` / `approved_on` from the API response (`get_calculations` in `api.py`) or the `Labs Calculation` DocType?
   - Note: the 11 Nov backlog (#26) keeps **approval states** in the governed tool registry, so removing them from the DocType may conflict with the backlog.

> i think ui only because the approved by and status should be only present i guess in other menu like calculation catalogue

---

## Applied from the answers (UI only, per Q5)

- **Q1, card view:** removed "Status" and "Approved by" from `CalculationCard.vue`.
- **Q2, details modal:** removed the status pill (header) and the "Approved by" field from `CalculationDetailsModal.vue`.
- **Q4, awaiting list / status counts:** these were no longer in the template, but `ToolsRegistryView.vue` still fetched them on load and after every action, without showing them. Removed that leftover code: `statusCounts`, `awaiting`, `countByStatus`, `refreshSummary`, `runAction`, and their imports.
- **Q5:** the API (`get_calculations`) and the `Labs Calculation` DocType are unchanged.
- `vue-tsc` and `vite build` pass.

## Still open

6. **Q2, part 2: Deprecate / Re-approve buttons.** "Yes" answered whether to remove the status pill and "Approved by". It's unclear whether the buttons in the modal footer should **stay** or be **removed**. They're status actions, so if status belongs in the Calculation Catalogue, they may belong there too. Left unchanged for now.

7. **Q3: status filter.** Not answered. The status dropdown is already commented out in `CalculationFilters.vue` (your frappe-ui `Select` work in progress). But `ToolsRegistryView.vue` still sets `filters.status = "Approved"`, so the registry **still lists only Approved calculations**, and there's no visible way to change that. Should it stay that way, or list all statuses?
