# General Implementation Plan

**Tech Stack:** Frappe v16 / Python, Managed PostgreSQL, DigitalOcean (Sydney), Vue 3, Frappe Redis Queue.

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
- the routes you used should, engineering-labs/*

**Status:** Pending

