# Task 13: DocType / Schema Design

Source: `guide_imgs/mockup-12.png`, with four tables: **Tool**, **Parameter**, **Calculation**, **Input Output**.

**Nothing is implemented yet.** Each question has a **suggested answer**. You can reply "use the suggestions", or answer only the ones you disagree with.

Task 12 (Q1 = B) saves the New Tool form into **Tool** and **Parameter**, so Task 12's Save button only works once this is built.

---

## 1. DocType names

The mockup says **Tool**, **Parameter**, **Calculation**, **Input Output**. The app already has a DocType called **`Labs Calculation`** (the current Tools Registry data), and all existing DocTypes use the `Labs` prefix. A plain "Calculation" would sit next to "Labs Calculation", which is confusing. "Tool" and "Parameter" are also very generic names on a shared Frappe site.

> **Suggested:**
>
> | Mockup       | DocType name          |
> | ------------ | --------------------- |
> | Tool         | `Labs Tool`           |
> | Parameter    | `Labs Tool Parameter` |
> | Calculation  | `Labs Tool Run`       |
> | Input Output | `Labs Tool Run Value` |
>
> `Labs Calculation` stays untouched. Replacing it is a separate decision.
> (Alternative for Calculation: `Labs Tool Calculation`, if you prefer to keep the word "Calculation".)

Answer: Let's just stick on what written in the board

---

## 2. Child tables or separate DocTypes?

The arrows show **Parameter → Tool** and **Input Output → Calculation**. In Frappe, that can be:

- **a child table:** the rows live inside the parent form, are saved together with it, and can't exist on their own;
- **a separate DocType with a Link field:** its own list and form, saved one by one.

Input Output also points to **Parameter** (Parameter ID). A Link field **can't point to a child table row**, so if Parameter is a child table, Parameter ID is stored as plain text (the row's ID). Frappe can't check that it exists.

> **Suggested:**
>
> - **Parameter = a child table of Tool.** The New Tool form saves the tool and its parameters in one go, which is exactly how the Task 12 form works.
> - **Input Output = a child table of Calculation.** One run saves its values together.
> - **Parameter ID** is stored as the parameter's row ID, and the field name is also copied in for readability.

Answer: Yes, good and seems correct suggestion, go.

---

## 3. Input Output "Calculation ID: Connection to Tool"

In the mockup, Input Output's **Calculation ID** is described as "Connection to **Tool**". The arrow goes to **Calculation**, though.

> **Suggested:** a typo; it means "Connection to **Calculation**".

Answer: for the input and output, actually i guess it is not finalized yet but I guess so since calculation have a connection to tools

---

## 4. Parameter's "Name: Primary Key"

Every Frappe record already has a built-in `name` column, its primary key, generated automatically.

> **Suggested:** use Frappe's built-in `name`; no extra field.

Answer: Okay

---

## 5. Add a "Label" field to Parameter

From Task 12 Q3 (answered "okay"): the form has a **Label** per row ("Load (kPa)") plus a **Field Name** (`load_kpa`). mockup-12 has no Label.

> **Suggested:** add **Label** (text, required) to Parameter.

Answer: okay

---

## 6. Field types

> **Suggested:**
>
> | DocType      | Field          | Frappe type                                  | Required |
> | ------------ | -------------- | -------------------------------------------- | -------- |
> | Tool         | Tool Name      | Data (unique)                                | Yes      |
> | Tool         | Type           | Select: Frappe / Excel / 3rd Party           | Yes      |
> | Tool         | iFrame URL     | Data                                         | Yes      |
> | Tool         | Tool Endpoint  | Data                                         | Yes      |
> | Tool         | Credentials    | **Password** (Frappe stores it encrypted)    | No       |
> | Tool         | Runtime Script | Code                                         | No       |
> | Tool         | Parameters     | Table (Parameter)                            |          |
> | Parameter    | Label          | Data                                         | Yes      |
> | Parameter    | Field Name     | Data                                         | Yes      |
> | Parameter    | Type           | Select: Input / Output                       | Yes      |
> | Parameter    | Data Type      | Select: Text / Date / Number                 | Yes      |
> | Parameter    | Mandatory      | Check                                        |          |
> | Calculation  | Tool ID        | Link → Tool                                  | Yes      |
> | Calculation  | Date and Time  | Datetime, defaults to now                    | Yes      |
> | Calculation  | Values         | Table (Input Output)                         |          |
> | Input Output | Parameter ID   | Data (the parameter row's ID)                | Yes      |
> | Input Output | Value          | Small Text (text, numbers and dates all fit) | No       |
>
> - **Tool Name is unique**, so the record's ID is the tool name, e.g. "Bearing Capacity".
> - **Field Name** must be unique within one tool and use only `a–z`, `0–9`, `_`. This is checked on save.

Answer: it's okay tho but I asked Sir Ton about security like if it needs the info to be encrypted and he said, I don't really mind it since frappe already do that security for me...

---

## 7. Who can create and edit

The other Labs DocTypes allow **System Manager** only.

> **Suggested:** the same for all four. Record-level access is deferred, per the 24 Nov notes.

Answer: just make it non role means open to all of roles, will update you here later.

---

## 8. Scope of Task 13

> **Suggested:**
>
> - **In scope:** create the four DocTypes and their validation; add `create_tool` in `api.py` for the Task 12 form.
> - **Not in scope:** screens for Calculation / Input Output (they're filled by "Run", which comes later), and edit or delete APIs. In Desk, System Managers can still view, edit and delete everything.

Answer: Okay

---

## Applied (25 Nov)

- **Q1:** names as on the board: **Tool**, **Parameter**, **Calculation**, **Input Output** (module Engineering Labs).
- **Q2:** Parameter is a child table of Tool; Input Output is a child table of Calculation.
- **Q3:** Calculation ID is the child row's built-in `parent`, i.e. the Calculation it belongs to.
- **Q4:** Frappe's built-in `name` is the primary key. Tool's ID is its Name (unique).
- **Q5:** Parameter has a Label field.
- **Q6:** the field types as suggested. Credentials is a Password field (Frappe encrypts it). Input Output also has an optional Field Name, copied from the parameter.
- **Q7:** Tool and Calculation give full access to the **All** role (every logged-in user). Update this when the roles are decided.
- **Q8:** `create_tool` in `api.py` (used by the Task 12 form). There are no edit/delete APIs and no Calculation screens; Desk can still do everything.
- **Database:** the DocTypes work on any database. The local site `cresco.local` is still **MariaDB**; moving it to PostgreSQL is a separate step (your choice A).

---

# Feedback: remove the other DocTypes

**Nothing is removed yet.** Deleting a DocType deletes **its table and every record in it**, and the code that reads it starts failing. So these need a clear yes first.

## F-1. Which DocTypes?

**Engineering Labs module (7):**

| DocType                                | Records      | Used by                                                                                       |
| -------------------------------------- | ------------ | --------------------------------------------------------------------------------------------- |
| Labs Calculation                       | 27           | Tools Registry list, Details modal, preview runner, Calculation Catalogue's "Add calculation" |
| Labs Calculation Input / Result / Note | (child rows) | Labs Calculation                                                                              |
| Labs Metric                            | 31           | Engineering Labs **Home** dashboard (metric cards)                                            |
| Labs Consistency Flag                  | 3            | Home dashboard (consistency flags panel)                                                      |
| Labs External API                      | 3            | Home dashboard (API health / quota panels)                                                    |

**Portal module (5):** Portal Stat, Portal News Post, Portal Team Member, Portal Event, Cresco Project. These are used by the Portal Dashboard and the Projects list (Calculation Catalogue).

> **Suggested:** only the **Engineering Labs** ones. The Portal ones belong to the Portal Core look and the project data.

Answer: well that's out of my scope, i mainly focus on engineering labs, so you can remove a doctype that associated with portal core and just make them as static ui

## F-2. What happens to the screens that use them?

| Option                  | What I'd do                                                                                                                                                                                                                                                              |
| ----------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **A. Remove all 7 now** | Delete them, remove their API functions and fixtures, and switch the Tools Registry to Tool (Task 11 F3). The **Home dashboard** loses its metric, flag and API panels (they'd show nothing or be removed). The Calculation Catalogue's "Add calculation" stops working. |
| **B. Step by step**     | First the **Labs Calculation** family (4 DocTypes) together with the Tools Registry switch. Keep Labs Metric / Consistency Flag / External API until the Home dashboard is redesigned.                                                                                   |
| **C. Keep all for now** | Don't remove anything until each screen has a replacement.                                                                                                                                                                                                               |

> **Suggested:** **B**. It removes what the new Tool replaces, without breaking the Home dashboard before its redesign.

Answer: B

## F-3. Calculation Catalogue's "Add calculation"

That modal picks a **Labs Calculation** and a project. Once Labs Calculation is removed, it has nothing to pick.

> **Suggested:** temporarily switch its picker to **Tool**, or hide the "Add calculation" button until the Catalogue is redesigned. Which do you prefer?

Answer: I think remove it since there's no add button in calculation catalog for my understanding

## F-4. Backup and data

- Deleting removes the records permanently from the database. The fixture files in the app (`fixtures/labs_*.json`) would also be deleted; git history keeps the files.

> **Suggested:** run `bench --site cresco.local backup` right before deleting, so the data can be restored if needed.

Answer: Can't git add .

tristanvic@Mana:~/cresco_engineering/apps/engineering_labs$ git add .
fatal: in unpopulated submodule 'apps/engineering_labs'
tristanvic@Mana:~/cresco_engineering/apps/engineering_labs$

## F-5. Git: the app's code isn't tracked (found while checking F-4)

Your `git add .` error (`in unpopulated submodule 'apps/engineering_labs'`) has a cause:

- The bench repo's first commit (`390367e`) saved `apps/engineering_labs` as a **submodule pointer** (a link to another git repo), not as files. That's because the app had its own `.git` folder at the time (`bench new-app` creates one).
- That inner `.git` folder **no longer exists**, and there's no `.gitmodules` file.
- **Result:** none of the app's code is in git right now. That covers the DocTypes, `api.py`, the whole Vue frontend, and the work from Tasks 1–13. Deleting a file would be unrecoverable.

So before deleting any DocType, the code needs to be in git. Two ways:

| Option | Commands (you run them) | Notes |
| --- | --- | --- |
| **A. Track the app inside the bench repo** | `git rm --cached apps/engineering_labs` then `git add apps/engineering_labs` then commit | Simplest. One repo for everything. |
| **B. Give the app its own repo** (Frappe's usual way) | `cd apps/engineering_labs && git init && git add . && git commit -m "..."`, then in the bench repo `git rm --cached apps/engineering_labs` | Needed if the app will be installed elsewhere with `bench get-app` (e.g. on the DigitalOcean server). |

> **Suggested:** **B**, since the app will be deployed to a server, which normally pulls each app from its own repo. Check with Sir Ton whether there's already a company repo for it.

Answer:
