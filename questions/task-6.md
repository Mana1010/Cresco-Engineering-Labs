# Task 6: Calculation Catalogue "Add" Modal: Questions

Task 6 is implemented. Where the plan was open, I used the defaults below. Please confirm or correct them.

1. **Which calculation is added?** The flow goes straight from picking a project (step 1) to Wind Classification (CheckWind) (step 2), as in mockup 11. There's no step for choosing which calculation to add. Should step 2 always be CheckWind for now, or should there be a way to pick the calculation, such as a step 0, or opening this flow from a calculation in the Tools Registry?
2. **What finishes the flow?** Step 2 has no "Save" or "Add to project" button; you can only close the modal with × or Escape, or go back to step 1. The result's log line mentions the project ("… · project #2026-0142 · …"), but nothing is saved. Should step 2 have a final button, and what should it do?
3. **Default project.** Nothing is pre-selected in step 1, so **Continue** stays disabled until you pick a project. Mockup 10 shows Riverside Apartments selected. Should the first project be pre-selected?
4. **"More details →" on project cards.** Static, like the other not-yet-built links. Where should it go eventually?
5. **"Rev A" badge.** Shown as static text from the mockup. What does the revision come from (calculation version, project revision, something else)?
6. **Demo projects.** Eight projects: the six from mockup 10, plus Bourkelands Childcare Centre and Glenfield Park Duplex so the list scrolls. The site addresses are invented, since the mockup only shows suburbs. They're in `public/js/portal/calculation_catalogue/projectsData.js`.
7. **Rest of the Calculation Catalogue page.** The page still shows the "This page hasn't been built yet" card under the new **Add** button. Is there a mockup for the catalogue list itself?
