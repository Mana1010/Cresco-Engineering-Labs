# Task 4: Collapsible Sidebar: Questions

The plan labels this task "Task 3" a second time, so I've named this file `task-4.md` to keep it separate from the Tools Registry questions. Should the plan heading be renumbered to Task 4?

The collapsible sidebar is implemented. Where the plan was open, I used the defaults below. Please confirm or correct them.

1. **Logo when collapsed.** "Cresco Australia" doesn't fit in the 72px collapsed sidebar, so it shows just "C". Once a logo image is set (`logoSrc`), the same image is shown smaller. Do you want a separate small logo, such as an icon mark, for the collapsed state?
2. **Engineering Labs when collapsed.** The submenu items (Home, Calculation Catalogue, Tools Registry) have no icons, so they can't show in icon-only mode. Clicking the Engineering Labs icon while collapsed expands the sidebar and opens the submenu. While you're on an Engineering Labs page, its icon is highlighted in blue. Is that OK, or would you prefer a pop-out menu next to the icon instead?
3. **Remembering the state.** The collapsed/expanded choice is saved in the browser, so it stays the same after a refresh and across pages. The default is expanded. Is that OK?
4. **Tooltips.** When collapsed, hovering an icon shows its name using the browser's built-in tooltip. Do you want a styled tooltip instead?
5. **Phone width.** On narrow screens the sidebar sits above the page. Collapsing turns it into a compact row of icons instead of the full list. Is that OK?
