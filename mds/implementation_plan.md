# General Implementation Plan

**Tech Stack:** Frappe v16 / Python, Managed PostgreSQL, DigitalOcean (Sydney), Vue 3, Tailwind, Frappe Redis Queue.

### Task Status Key

- **Not Complete** – Not yet implemented. Do not implement unless explicitly instructed by the developer.
- **Pending** – Awaiting AI implementation.
- **Complete** – Implemented and reviewed by the developer.

### General Instructions

- If any requirement is unclear, ambiguous, or requires clarification or confirmation, ask the developer before proceeding.
- If you have questions, create a `questions/` folder in the project root.
- Create a separate Markdown question file for each task, using the format `task-<number>.md` (e.g., `task-1.md`).
- List all questions clearly in the corresponding file. Include enough context for the developer to understand what needs clarification.
- Do not mix questions from different tasks in the same file.
- If there are no questions for a task, creating a question file is unnecessary.
- Do not make assumptions or implement features beyond the explicitly stated requirements.

### Question File Structure

```text
questions/
├── task-1.md
├── task-2.md
└── task-3.md
```

Each file should contain a list of questions related only to its corresponding task.

## Task 1: Sidebar UI Implementation

### Reference Images

Located in the `guide-imgs/` folder. Multiple reference images may be provided by the developer.

Images: mockup-1

- Follow the arrows and annotations in the reference images as implementation guidance.
- The developer is responsible for providing and uploading the reference images.

### Requirements

- Recreate the sidebar shown in the reference images using Vue 3 within Frappe v16.
- Existing sidebar menus should be static and non-clickable.
- Add an **Engineering Labs** dropdown menu below the arrow, containing:
  - Home
  - Calculation Catalogue
  - Tools Registry
- Only the Engineering Labs dropdown should be clickable. Do not implement submenu functionality or navigation yet.

**Status:** Completed

## Task 2: Engineering Labs > Home UI Implementation

### Reference Images

Located in the `guide-imgs/` folder. Multiple reference images may be provided by the developer.

Images: mockup-2, mockup-3,mockup-4

- The developer is responsible for providing and uploading the reference images.

### Requirements

- Implement me a home page containing all those cards and graphs you see in mockup 2 and mockup 3
- In mockup 2, you should remove I guess the title and included the paragraph below the title, it has an arrow on it
- In mockup 2 and 3, that cards you see should implemented all in home, it should be responsive like those cards
- In mockup 4, the 1 and 2 arrows should be still displayed or fix when the user tried to navigate in engineering labs submenus,
- when the user clicked the engineering labs > submenus, they should be highlighted
- The color, feels, should match the vibes so that the ui is consistent.
- the routes you used should, engineering-labs/\*

**Status:** Completed

## Task 3: Engineering Labs > Tool Registry Implementation

### Reference Images

Located in the `guide-imgs/` folder. Multiple reference images may be provided by the developer.

Images: mockup-5, mockup-6

- The developer is responsible for providing and uploading the reference images.

### Requirements

- in mockup 5, can you please add it in tool registry section those boxes
- in mockup 5, in arrow 1, please change it to the toggleable two buttons, these buttons associated the design or structure of those tool registries, example one button for box or grid design of tool structure, the other one is a table design resemblance in mockup 6, use icon only.
- in mockup 5, in arrow 2, please remove it, instead there are only like small title above the div of those boxes named "All Calculations"
- in mockup 5, in arrow 3, you should add a boxes like in mockyp 6 arrow 3 in the top of the boxes
- in mockup 5, in arrow 4, you should add the awaiting approval just like in mockup 6 arrow 4, you should slightly change the design my stack up those awaiting approval like same vibes in mockup 5 boxes but make them like 100% width box and add a button "Show Calculation" along with accept and return to draft and also add a small text from top of those awaiting approval named "Awaiting Approval"
- In mockup 6, in arrow 5, you should add it between in awaiting approval and all calculation, this is only applicable to those calculation
- add a infinite scrolling, 15 items the limit until it loads again for another 15 items
- in awaiting approval, if ever it getting more and more, you should add a height limit and make them scrollable to not eat the whole screen.

## Feedback

- Can you please set a fix width, because when i select the or change something in filter, the width is slightly moving and its because of the mousebar in the right, so its up to you.
- Also the calculation change the color or something that indicate being hovered by the cursor
- Can you also add a search bar bellow the "Add Calculations" title for All Caculations

## Feedback V2

- When the search not found, create a ui for empty or not found purposes, don't just use the loading as fallback.
- Can you add a "Add" button in Tools Registry where the user can Add a tool, just make it a static only.
- In Awaiting Approval, can you please show a modal when the user click the Show Calculation button, just same in Task 5 but remove the Deprecated button.
  **Status:** Completed

## Task 4: Collapsible Sidebar

### Reference Images

Located in the `guide-imgs/` folder. Multiple reference images may be provided by the developer.

Images: mockup-7

- The developer is responsible for providing and uploading the reference images.

### Requirements

- In mockup 7, in the arrow, can you please make the sidebar collapsible by clicking the menu icon from the arrow, when collapsed, only the icons are visible but when opened then icon + text like same in the picture.

## Feedback

- It's working but I noticed when the sidebar is collapsed and tried to click the engineering labs button, it triggers the sidebar to be un-collapse again and a slight ui bug, can you also make those submenus also visible when the sidebar is collapsed? like when the user hover it or clicked it, it will show a small modal contains those submenus (this only happens during collapsed sidebar)

## Feedback V2

- When the user click the engineering labs, by default it should be navigated to the engineering-labs/home route.
- I noticed, when i click the specific menu, the other menu moved, can you fix it.

**Status:** Pending

## Task 5: Showing Tool Registry Details

### Reference Images

Located in the `guide-imgs/` folder. Multiple reference images may be provided by the developer.

Images: mockup-8, mockup-9

- The developer is responsible for providing and uploading the reference images.

### Requirements

- when the user click one of the tool registry box or the row if it is in table mode then there will be a modal appearing in the center of screen and that is the mockup-8 and mockup-9
- in mockup 8, in arrow 1 when the director/admin click it, it will mark the box or that tool as deprecated and it will also look like in mockup 8 in the right, then the director can Approve & and Publish it, I guess just include the Re-approve button and remove the other one.
- Next is in mockup 8, when the user click that button in arrow 2, it will show the modal like that in mockup 9, it should be empty first like in the mockup 9 left image unless the user click the Run via... button then it will show the calculation like in the right image of mockup 9

### Feedback

- when i open the modal, there's like a white thick line that is showing in the right corner, can you please remove it

**Status:** Completed

## Task 6: Adding Calculation Catalogue Modal

### Reference Images

Located in the `guide-imgs/` folder. Multiple reference images may be provided by the developer.

Images: mockup-10, mockup-11

- The developer is responsible for providing and uploading the reference images.

### Requirements

- In Calculation catalogue, can you please add a single "Add" Button
- When the user click that button, the modal should show up in the center, use the design in mockup-10 but increase the width of modal
- in mock up 10 after clicking continue, it will show the step 2 in modal also which is the mockup 11, in the left side are the inputs and the right side are the calculation result, in input the site address should be based on the selected project as default then include the standard edition and structured height then also by default, the calculation result are already display in the right side.
- the Step 1 and Step 2 should be changing depends on which page the user is currently.

**Status:** Completed

## Task 7: All Data from POC should be transfer as Doctype

### Reference Images

Located in the `guide-imgs/` folder. Multiple reference images may be provided by the developer.

Images: Cresco_Engineering_Labs_POC_v0_7

- The developer is responsible for providing and uploading the reference images.

### Requirements

- All data in the POC can you make it into doctype
- All the mockup data in the POC can you also save it in fixture so that the other dev who later clone the app can benefits from it.
- Also add a module named Cresco Portal in the desk or main page and when clicked, it will navigate to the /portal route

**Status:** Pending
