# Task 3: Engineering Labs > Tools Registry: Questions

Task 3 is implemented at `/engineering-labs/tools-registry`. Where the plan was open, I used the defaults below. Please confirm or correct them.

1. **Filter and toggle placement.** The type and status filters (mockup 6, arrow 5) sit on the same row as the "All Calculations" title, next to the grid/table toggle (arrow 1). That puts them between Awaiting Approval and the calculation boxes, and they filter only the All Calculations list. Is that layout OK, or do you want the filters on their own row?
- The filters are okay 
2. **Approve / Return to draft.** These work on the demo data in the browser only. Approve marks the item Approved with your name and today's date. Return to draft marks it Draft. Either way the item leaves Awaiting Approval and the stat boxes update. A page refresh resets everything, because there is no backend yet. Is that fine for now?

- Yes
3. **Show Calculation.** The button is there but does nothing, because there is no calculation detail page yet. The same goes for the → button on each card and the › at the end of each table row. What should these open?

- the calculation is clickable for this task, let them unclickable for now
4. **What "All Calculations" includes.** It lists every status (Approved, Awaiting approval, Draft, Deprecated), so items awaiting approval appear both in the Awaiting Approval list and in All Calculations. Should All Calculations show only Approved items by default, like the mockup 6 table?

- I guess much better by default only the approved items
5. **Types.** The type filter offers API, Python and Excel. The mockups only show API and Python; I added Excel because the home page lists Excel tools, such as Wind Pressure (Excel). Is that right?

- Yes
6. **Demo data.** There are 27 demo calculations (20 approved, 5 awaiting approval, 1 draft, 1 deprecated), so infinite scroll has more than one batch of 15 to load. The names come from mockups 5 and 6 and the home page tool list, plus some invented ones. Everything is in `public/js/portal/tools_registry/registryData.js`. `fetchCalculations()` already takes offset, limit and filters, so it can later be swapped for a real backend call.

- Well, can you at least do a pagination using the infinite scrolling with like a loading animation at the button when the user tried to scroll down 
7. **Awaiting Approval height limit.** The list stops growing at 420px and scrolls inside itself after that, which is about 3½ cards on desktop. Is that a good height?

- decrease the height since it takes almost the screen, adjust also the height of the boxes
8. **Remembering the view.** The grid/table choice resets to grid when you leave the page. Should it be remembered?

- I guess much better, the default is the box
9. **Dashboard is now clickable** (your answer to Task 2, question 3). It goes to `/portal`. The other main menu items are still static.
- It's okay