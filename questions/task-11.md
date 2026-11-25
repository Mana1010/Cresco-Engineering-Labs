# Task 11: Redesign Tools Registry

Source: the Claude artifact in the plan (canvas "Calculation Cards"). I read its Tools Registry artboards.

**Nothing is implemented yet.** The questions below change what gets built. Each one has a **suggested answer**, so you can reply "use the suggestions" or answer only the ones you disagree with.

---

## 1. Which artboard is the design?

The link opens `#page-d1c2e59ea5a1`, but that page **no longer exists** in the artifact. The canvas now has these Tools Registry artboards:

| Artboard                                                        | Page                                       | What it shows                                                                                                                                                                 |
| --------------------------------------------------------------- | ------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Tools Registry — List view** (`ToolsList`)                    | "List of Official Engineering Labs Design" | List view by default, **sortable** Calculation / Type / Category headers, a Filter popover with a **Type** dropdown, a "Showing X of 14 tools" footer, and a grid view toggle |
| **Tool Registry Filter** (`ToolsFilter`)                        | "List of Official Engineering Labs Design" | The same design in grid view, with the Filter popover open                                                                                                                    |
| **Tools Registry** (`ToolsModern`)                              | (no page set)                              | Grid by default, a Filter popover with **Type chips (with counts) + a Category dropdown**, filter chips with "Clear all"                                                      |
| Copies (`ToolsList-sq4y`, `ToolsList-8i2n`, `ToolsFilter-wsz4`) | "Tool Page"                                | Identical copies                                                                                                                                                              |

> **Suggested:** use **ToolsList + ToolsFilter**. They're on the "Official" page and are one consistent design (list and grid views, a Type filter).

Answer: idk about this also

## 2. Default view: list or grid?

ToolsList opens in **list** view; ToolsFilter and ToolsModern open in **grid** view. The current page remembers the user's last choice (stored in the browser) and defaults to grid.

> **Suggested:** keep remembering the last choice, and default to **list** (the official ToolsList).

Answer: Grid

## 3. Sortable column headers (list view)

ToolsList has clickable **Calculation / Type / Category** headers that sort the list. The registry currently loads tools **15 at a time while scrolling** (infinite scroll), sorted by name on the server. Sorting only the loaded rows would be wrong once more tools load. Doing it properly needs a small change to `get_calculations` in `api.py` (an allowed `order_by` parameter).

> **Suggested:** add server-side sorting: a small, safe change to `get_calculations` that accepts only those three fields.
> Alternative: show the headers without sorting for now.

Answer: idk about this, just select the best

## 4. "Showing X of N tools" footer vs infinite scroll

ToolsList ends with **"Showing 14 of 14 tools"**. The current page uses infinite scroll, with "Loading more…" and "You've reached the end of the list."

> **Suggested:** keep infinite scroll, and replace the end message with the design's footer "Showing {loaded} of {total} tools".

Answer: No infinite scroll, will send a sample image in prompt message

## 5. "All Tools" tab with a count

The design has a single **All Tools** tab with a count badge (the tab area is ready for more tabs later).

> **Suggested:** add it, with the count = the total number of tools from the API.

Answer: sure

## 6. Autonomous badge

The current cards and rows show an orange **"Autonomous"** badge. The **design doesn't show it**: the data has the field, but nothing displays it.

> **Suggested:** remove the badge, to match the design.

Answer: remove the autonomous badge, we did not mention about autonomous

## 7. Type pill colours

The design gives each type its own colour: **API = indigo**, **Python = sky blue**, **Excel = green**. The list view also shows a small icon in the pill. Currently all types use the same blue.

> **Suggested:** follow the design's colours (and the icons in the list view).

Answer: sure

## 8. Page title, description and font sizes

Without the breadcrumb (removed, per the requirement), the design's header is:

- **Tools Registry** (24px, bold)
- _"Every calculation tool available in Engineering Labs — APIs, Python services and protected Excel workbooks."_

The design also uses larger text than the current page (14–16px vs 10–13px) and the font **Segoe UI**. The portal uses its own font.

> **Suggested:** add the title and description; use the design's sizes and colours; keep the **portal's font** so the page matches the rest of the portal.

Answer: okay, let's see

## 9. Filter contents

ToolsList's Filter popover has only a **Type** dropdown, with Clear / Done. A badge "1" shows on the Filter button and a "Type: X ×" chip appears when a type is selected. The status filter stays hidden, still defaulting to Approved, as now (Task 10 Q3 is still open).

> **Suggested:** build it exactly like that.

Answer: yup

## 10. "New Tool" button

The design's button says **"New Tool"** (the current one says "Add"). Adding a tool isn't implemented.

> **Suggested:** rename it to "New Tool" and keep it static (does nothing yet).

Answer: yes

---

**Not changed:** clicking a tool still opens the existing details modal. The design doesn't cover what happens on click.

**Feedback** make the color of the button like "New Tool" in this color: #232936

---

## Applied from the answers

- **Q1:** used **ToolsList + ToolsFilter** (the "Official" page) since no preference was given.
- **Q2:** defaults to **grid**; the user's last choice is still remembered.
- **Q3:** **server-side sorting**: click Calculation / Type / Category in the list view to sort, and click again to turn it off. `get_calculations` accepts `sort` = `name` / `type` / `category` only; anything else falls back to the default order.
- **Q4:** **infinite scroll removed**, replaced by **numbered pagination** at the bottom right (‹ 1 2 3 4 5 ›, up to 5 numbers, centred on the current page). The footer's left side shows "Showing 1–9 of 20 tools". **9 tools per page** (three full grid rows).
- **Q5:** **All Tools** tab with the total count.
- **Q6:** **Autonomous badge removed** from the cards, the list rows and the details modal.
- **Q7:** type colours: **API indigo, Python sky blue, Excel green**, with icons in the list view.
- **Q8:** added the title and description, and the design's sizes and colours; kept the portal font. No breadcrumb.
- **Q9:** Filter popover with a Type dropdown + Clear / Done, a "1" badge, and a removable "Type: X" chip.
- **Q10 + feedback:** **New Tool** button in **#232936** (slightly darker on hover); static.
- **Hover states from the design:** cards get a blue border and glow, a blue title and a filled blue arrow; list rows get a light-blue background, a blue title and a filled blue arrow; sort headers, filter, tabs and pagination buttons all have hover states.

**Still open:** Task 10 Q3. The hidden status filter still lists **Approved** tools only.

## Feedback 2: fit-to-screen pagination (25 Nov)

No choices were given, so I used my suggestions:

- **Tools per page** = what fits between the toolbar and the pagination footer without scrolling the page. It's re-checked when the window is resized, when switching grid/list, and when the filter chip appears or disappears.
- **Grid:** full rows only, 6 to 18 tools (3 columns; 2 columns below 1100px wide, 1 below 640px).
- **List:** 6 to 20 rows.
- **On resize:** stays on the page that holds the first tool you were looking at.
- **Checked in the browser:**

  | Height | Grid | List |
  | --- | --- | --- |
  | 560px | 6 (minimum) | |
  | 720px | 6 | 6 |
  | 1065px | 12 | 10 |
  | 1600px | 18 | 17 |

  From page 2 at 1065px, shrinking to 720px kept "Slab on Ground" as the first tool shown.

---

# Feedback 3: show newly added tools in the Tools Registry

**Not implemented yet.** These depend on Task 13's feedback (removing the old DocTypes), so please answer both together. Each has a **suggested answer**.

## F3-1. Switch the list to the new Tool DocType?

The registry currently lists **Labs Calculation** (27 records, 20 of them Approved). New tools are saved to **Tool**.

| Option | Result |
| --- | --- |
| **A. Tool only** | The registry shows only tools added with New Tool. It starts **empty** until you add some. |
| **B. Both** | Labs Calculation and Tool mixed in one list. Messy: different fields, two ID systems, and Labs Calculation may be deleted (Task 13). |

> **Suggested:** **A**, since Task 13's feedback removes Labs Calculation anyway.

Answer:

## F3-2. What the card and row show

The cards show **source** ("Workbook · AS 2159"), **version** and **category**. Tool has **none** of these. It has Name, Type, iFrame URL, Tool Endpoint and Parameters.

> **Suggested:**
>
> - **Card:** type pill, tool name, the endpoint's website as the grey subtitle (`tools.example.com`), and **"3 inputs · 2 outputs"** pills where version and category were.
> - **List columns:** Tool, Type, Inputs / Outputs. Sortable by Tool and Type.
> - Alternative: add Source / Version / Category fields to Tool (a schema change, Task 13).

Answer:

## F3-3. Status filter

The registry shows **Approved** Labs Calculations only. Tool has no status.

> **Suggested:** show **all** tools.

Answer:

## F3-4. Clicking a tool

The Details modal is built for Labs Calculation: Approve/Deprecate, notes, and "View calculation" (preview runner). None of that exists for Tool.

> **Suggested:** a simple **read-only details** modal: name, type, iFrame URL, endpoint, and the inputs/outputs table. The "Use tool" modal (left panel + iframe) is a later task.
> Alternative: clicking does nothing for now.

Answer:

## F3-5. After saving in New Tool

> **Suggested:** refresh the list and the **All Tools** count, so the new tool appears straight away.

Answer:
