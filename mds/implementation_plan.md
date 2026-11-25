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

**Status:** Completed

## Task 8: Implement Frappe UI to Sidebar

### Reference Images

Located in the `guide-imgs/` folder. Multiple reference images may be provided by the developer.

Images:

- The developer is responsible for providing and uploading the reference images.

### Requirements

- Translate the code of sidebar to frappe UI ready made components using Sidebar

**Status:** Completed

## Task 9: Implement Frappe UI to Tools Registry Table

### Reference Images

Located in the `guide-imgs/` folder. Multiple reference images may be provided by the developer.

Images:

- The developer is responsible for providing and uploading the reference images.

### Requirements

- Translate the code of tools registry list table to frappe UI ready made components using List or other related to Table

**Status:** Completed

## Task 10: Remove Approved By and Status in Tools Registry

### Reference Images

Located in the `guide-imgs/` folder. Multiple reference images may be provided by the developer.

Images:

- The developer is responsible for providing and uploading the reference images.

### Requirements

- Remove the approved by and status column and also the data of it in tools registry.
  **Status:** Completed

## Task 11: Redesign Tools Ragistry

### Reference Images

Located in the `guide-imgs/` folder. Multiple reference images may be provided by the developer.

Images / Link: https://claude.ai/artifact/Lab8xXuHUz3CBgcgeWHFGM?sk=OXMIEdfSbwdBNp4plTcaLQ#page-d1c2e59ea5a1

- The developer is responsible for providing and uploading the reference images.

### Requirements

- Please redesign the tools registry using these design generated by the claude artifacts
- Remove the breadcrumbs in the top of the title
- Please be aware that there's a hover color changes, just in case you forgot, it is included in the claude artifact link

## Feedback

- Can you please remove the title along with the brief description from the top?
- I noticed, when i click some number in pagination, it navigate back to the top, can you make it not movable? like stay on the screen when the user click the pagination number

- Can you also change the 3 sockets or type, from Api, Excel and Python, named it to Frappe, Excel and 3rd Party

## Feedback 2

- Please implement the "fit to screen" pagination

## Feedback 3

- Please implement now or display the newly added tool in Tools registry

  **Status:** Pending

## Task 12: New Tool Form

### Reference Images

Located in the `guide-imgs/` folder. Multiple reference images may be provided by the developer.

Images / Link: https://claude.ai/artifact/Lab8xXuHUz3CBgcgeWHFGM?sk=OXMIEdfSbwdBNp4plTcaLQ#page-fe7caaa782dd

- The developer is responsible for providing and uploading the reference images.

### Requirements

- Can you implement the design from the claude artifact link, use frappe ui for modal, inputs, dialog, etc. but use non frappe ui if the design are very far from the design, for buttons I guess use the non frappe ui
- Implement also the confirmation dialog, this is when the user accidentally click cancel, or the exit one without finishing the form. (Will run only if the user triggered the input like it already has a progress but if non then don't trigger the confirmation dialog)
- For accidental refresh, implement the beforeunload or something to trigger the confirmation before being load completely, (if possible for beforeunload, trigger the dialog I just design instead of the default one for modern but don't force if not)
- save the temporary session in local storage or cookie for new tool form modal so that it persist.

- Please fix the height problem where when i tried to add more input, it affects the content or body scroll, make in the section of parameters scrollable only when the user tried to make more inputs so that it will not affect the content or if you have a more modern idea for this, just implement it.
- my bad, can you please remove the scroll again of parameters, just use the scroll of form, because it seems more cleaner to me and more spacious
  **Status:** Completed

## Task 13: Doctype / Schema Design

### Reference Images

Located in the `guide-imgs/` folder. Multiple reference images may be provided by the developer.

Images: mockup-12

- The developer is responsible for providing and uploading the reference images.

### Requirements

- Check the image and build it as doctype / table I guess, that is not yet finish but yeah that's our doctype and the fields associated with the doctype.

## Feedback

- Can you please remove the other doctype except to those new 4 doctypes, don't remove it yet if you are unsure, just make a question again

  **Status:** Pending
