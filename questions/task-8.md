# Task 8: Implement Frappe UI to Sidebar: Questions

Task 8 is implemented in `frontend/src/portal/Sidebar.vue`. The decisions below were confirmed by the developer on 2026-11-02. Please check them with Ton.

**How frappe-ui's `Sidebar` compares with the Cresco design**

| Current sidebar | frappe-ui `Sidebar` |
|---|---|
| Dark (`#231f20`), white bold 11px labels, blue (`#00a0e3`) active pill | Light grey surface, grey 14px labels, active row is a raised white tile. No theme or colour props |
| Brand + blue divider + blue bar at the bottom | `SidebarHeader` is a 48px row with a square logo. Custom markup is allowed in the slot instead |
| Collapsed: Engineering Labs flyout submenu | Collapsed: icons with tooltips. No flyout |
| Clicking "Engineering Labs" expands the submenu and goes to Home | `SidebarSection` only opens/closes. It can't navigate |
| Items without pages are plain, non-clickable text | A `SidebarItem` without a route is a button |

**Decisions**

1. **Look: keep the Cresco design**, built from frappe-ui's `Sidebar` and `SidebarItem`. The dark theme, blue active pill and fonts are restored with CSS that targets frappe-ui's documented `data-slot` / `data-state` attributes, not its internal class names. Expanded, the sidebar is pixel-identical to before.
2. **Engineering Labs keeps the agreed behaviour.** It's a `SidebarItem` with its sub-items under it, not `SidebarSection`, because a section can't navigate. Outside Engineering Labs, a click goes to Home and opens the submenu. Inside, a click opens/closes the submenu.
3. **Collapsed: frappe-ui tooltips, no flyout.** Hovering an icon shows its name. Clicking Engineering Labs while collapsed goes to Engineering Labs Home.
4. **Items without pages** (Projects, Proposals, Deliverables, Inspections, Analytics, Desk) are shown but disabled.
5. **Mobile (≤768px)** keeps the current stacked layout.
6. **Logo** keeps the current "CRESCO / AUSTRALIA" text.

**Findings for the frappe-ui assessment**

- **Fits:** the structure (`<nav>` landmark, rows, router links with automatic active state), the collapse state (`:collapsed`, driven by the header's menu button and saved in the browser), the width props, and the collapsed tooltips.
- **Doesn't fit without overrides:** the colours, font sizes, row padding and active style. There are no props for these, so the Cresco look is about 150 lines of CSS overrides on frappe-ui's markup. Those overrides may need updating if frappe-ui changes its sidebar markup.
- **Not available:** a collapsed flyout submenu, or a collapsible group that also navigates.
