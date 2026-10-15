# Task 1: Sidebar UI Implementation: Questions

The sidebar is implemented. The plan didn't cover the points below, so I used a default for each. Please confirm or correct them.

1. **Page route.** The sidebar is served as a standalone Frappe web page at `/hub` (`engineering_labs/www/hub.html`). The other options were a Desk page or replacing the Desk sidebar. Is `/hub` the right route and approach, or should it live somewhere else?

Answer: use the /portal
2. **Login requirement.** `/hub` is currently reachable by Guest users. Should it require login?
Answer: Yes much better, frappe already have a login method so just use it.
3. **Logo.** No logo file was provided, so "CRESCO / AUSTRALIA" is drawn with CSS text. Can you supply the official logo (SVG preferred) to replace it?
Answer: Just put it as placeholder (use image) > add a variable then just add it as null and do this imageSrc or Placeholder (Cresco Australia)

4. **Icons.** The menu icons are inline SVG approximations of the mockup. Is there an icon set you want to use instead, such as Frappe's built-in icons, Font Awesome or Lucide?
Answer: I think use your own menu icons specifically an svg one.
5. **Active state.** "Dashboard" is shown highlighted, as in the mockup. Should it stay highlighted while everything is static?
Answer: Yes
6. **Dropdown default.** The Engineering Labs dropdown starts collapsed. Should it start expanded?
Answer: Not yet, just stay what it is 
7. **Main content area.** Only the sidebar is built. The header ("Welcome back, …") and the dashboard cards in the mockup were left out because they aren't in the Task 1 requirements. Is that correct?
Answer: Yup but I want you to also build the rest like in the reference image 
8. **App installation.** `engineering_labs` is not installed on `cresco.local` yet, so `/hub` returns 404 until you run `bench --site cresco.local install-app engineering_labs`. I didn't change the site database without your go-ahead.
Answer: Already done and run
