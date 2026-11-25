# Task 12: New Tool Form

Source: the Claude artifact in the plan (canvas "Calculation Cards"). I read the **New Tool modal** and **New Tool: discard confirmation** artboards.

**Updated after Task 13 was added.** Task 12 is now the **New Tool form only** (no Edit form), and Task 13 owns the DocType / schema (`guide_imgs/mockup-12.png`). So I removed or changed these questions:

- **Removed:**
  - how to open the Edit form (Edit is no longer in this task);
  - the DocType field list (now Task 13);
  - the Type names (mockup-12 says **Frappe, Excel, 3rd Party**);
  - the data types (mockup-12 says **Text, Date, Number**).
- **Changed:**
  - Q1 is now about connecting the form to the Task 13 DocTypes;
  - Q3 is new: the form has a **Label** that the schema doesn't have.

**Nothing is implemented yet.** Each question has a **suggested answer**. You can reply "use the suggestions", or answer only the ones you disagree with.

---

## 1. Should "Save Tool" save into the Task 13 DocTypes?

Task 12's requirements only describe the **form**. Task 13 creates the **Tool** and **Parameter** DocTypes (mockup-12). They connect naturally: Save Tool → one Tool record + its Parameter rows.

| Option                                                                                                                                             | Result                               |
| -------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------ |
| **A. UI only.** The form works (validation, confirmation, draft), but Save only closes it with a message. Nothing is stored.                       | Tasks 12 and 13 are shown separately |
| **B. Connected.** Build Task 13 first, then Save Tool calls a small whitelisted API (e.g. `create_tool`) that creates the Tool and its Parameters. | A saved tool you can open in Desk    |

> **Suggested:** **B**, since the 24 Nov notes ask for "DocType and basic CRUD" by 26 Nov. This task adds only the **create** API; edit and delete aren't in Task 12.

Answer: B

### 1a. (If B) Should the Tools Registry list show the new Tool records?

The list currently shows `Labs Calculation` records, so a newly saved tool **won't appear** in the list.

> **Suggested:** **not in this task.** Keep the list as it is and show a "Tool saved" toast. Switching the list (cards, filters, sort, details) to the new Tool DocType is a bigger change and should be its own task.

Answer: Yah

---

## 2. Which artboard is the design?

The plan link opens `#page-fe7caaa782dd`, but that page **doesn't exist** in the artifact. The "New Tool Form" page has:

- **New Tool modal copy** (`NewToolModal-7yft`), identical to `NewToolModal` on the Official page;
- **New Tool: discard confirmation** (`NewToolConfirm`), the same modal with a "Discard this new tool?" dialog on top.

> **Suggested:** use these two.

Answer: use those two

---

## 3. Label vs Field Name (the design and mockup-12 differ)

- **The design** has a **Label** for each row ("Load (kPa)"), with the **field name** generated under it (`load_kpa`).
- **mockup-12's Parameter** has **Name** (primary key) and **Field Name**, but **no Label**.

So where does the label go?

| Option                                              | Form                                              | Schema          |
| --------------------------------------------------- | ------------------------------------------------- | --------------- |
| **A.** Add a **Label** field to Parameter (Task 13) | As designed: label + field name                   | One extra field |
| **B.** Field Name only                              | One input per row (`load_kpa`); no readable label | As mockup-12    |

> **Suggested:** **A.** The label is what staff will see in the left panel later ("Load (kPa)"), and the field name is the JSON key for the tool.

Answer: okay, let's see for your suggestion

### 3a. Can the admin edit the field name?

The design shows the field name as a **read-only tag** generated from the label. It must match the key the tool expects, and the generated one may not ("Building Height" → `building_height`, but the tool may expect `height_m`).

> **Suggested:** keep the design's look, but **click the tag to edit it** with a small inline input. It auto-generates until the admin edits it. An invalid name (only `a–z`, `0–9`, `_`, not starting with a number) or a duplicate one shows red, and Save is blocked.
> Alternative: read-only, exactly as the design.

Answer: yes, admin can edit it to make it more flexible

---

## 4. Form fields vs mockup-12

These match, so they just need a yes:

- **Type dropdown:** Frappe / Excel / 3rd Party (the design said Frappe, API, Python, Excel).
- **Data type dropdown:** Text / Date / Number (the design also had Select and Check, which mockup-12 doesn't).
- The **Required** checkbox saves to Parameter's **Mandatory**.
- **Runtime Script** stays a **disabled "Coming later"** field, as in the design. It exists in the schema, but the 24 Nov notes say not to implement it yet.

> **Suggested:** yes to all four.

Answer:yes

---

## 5. Starting values

The design is pre-filled with sample data (Bearing Capacity, 3 inputs, 2 outputs, a credential).

> **Suggested:** start **empty**, with one blank input row and one blank output row.

Answer: Just blank, empty also will add a design for empty parameter

---

## 6. Confirmation dialog: when it appears

Requirement: show it on Cancel or close when the form has progress, but not when it's untouched.

> **Suggested:**
>
> - It's triggered by **Cancel, ×, Esc, and clicking outside** the modal.
> - **"Has progress"** means anything was typed, chosen, or any row was added or removed.
> - The dialog's list ("Bearing Capacity: tool registration details", "3 inputs and 2 outputs") uses the real values.

Answer: idk about this but implement this

---

## 7. Refresh warning (beforeunload)

Browsers **don't allow a custom dialog** on refresh or tab close. The page can only ask the browser to show its **own** "Leave site?" box, and the text can't be changed. All modern browsers behave this way.

> **Suggested:** use the browser's built-in box on refresh/close (only when the form has progress), and use your custom dialog for Cancel / × / Esc / clicking outside. Your requirement already allows this ("don't force if not").

Answer: sure

---

## 8. Draft saved in local storage

Requirement: keep the New Tool form's progress in local storage or a cookie.

> **Suggested:**
>
> - Use **local storage** (cookies are sent to the server on every request and are size-limited).
> - **Don't store the Credentials field** in the draft. Local storage is plain text in the browser, so an API key would sit there unprotected. After a refresh, the admin retypes it.
> - **Restore automatically** when New Tool is opened again, with a small note "Draft restored" and a "Start over" link.
> - **Clear the draft** after Save or "Discard changes".

Answer: yess

---

## 9. Frappe UI vs custom

Requirement: Frappe UI for the modal, inputs and dialog; custom buttons; custom anywhere the design is far from Frappe UI.

The design's inputs are **38px tall with a sky-blue focus ring**. Frappe UI's are 28–32px, grey-filled, and borderless, so they look quite different.

> **Suggested:**
>
> - **Frappe UI `Dialog`** for the modal shell and the confirmation dialog (focus trap, Esc, click outside).
> - **Custom** inputs, selects and buttons, to match the design.
> - Alternative: Frappe UI `TextInput` / `Select` restyled with CSS to look like the design.

Answer: Okay

---

## 10. Save validation and what happens after saving

> **Suggested:**
>
> - **Required:** tool name, type, iframe URL, endpoint, and at least one input. URLs must start with `http://` or `https://`.
> - Every parameter row needs a label and a valid field name.
> - **After saving:** close the modal, show a "Tool saved" toast, and clear the draft.

Answer: sure

---

## Applied (25 Nov)

- **Q1 B:** Save Tool posts the form to `create_tool`. That API and the Tool / Parameter DocTypes are **Task 13** (see `questions/task-13.md`), and are now built, so Save stores the tool (25 Nov).
- **Q1a:** the list is unchanged; a saved tool doesn't appear in it.
- **Q2:** built from `NewToolModal-7yft` + `NewToolConfirm`.
- **Q3 / Q3a:** Label + field name. The field name is generated from the label and is editable by clicking its tag. Clearing it hands it back to the label. Invalid or duplicate names show red and block Save.
- **Q4:** Type = Frappe / Excel / 3rd Party; data type = Number / Text / Date; Required → Mandatory; Runtime script disabled.
- **Q5:** starts blank with no rows. The empty parameter message is a **placeholder** until your empty-state design arrives.
- **Q6:** Cancel, ×, Esc and clicking outside ask for confirmation only when something has been entered.
- **Q7:** the browser's own "Leave site?" box on refresh or tab close, while the form has progress.
- **Q8:** a draft in local storage (no credentials), restored with a "Start over" link, and cleared on Save or Discard.
- **Q9:** frappe-ui `Dialog` for both dialogs; custom inputs, selects and buttons.
- **Q10:** name, type, both URLs (http/https) and at least one input are required; each row needs a label and a valid field name. After saving: a toast, the draft is cleared, and the modal closes.

### Feedback: the form height when adding parameters (25 Nov)

- The modal stays inside the screen: the header and footer (with Save) stay in place, and only the body scrolls.
- ~~Each Inputs / Outputs list scrolls on its own after about 4 rows.~~ Removed after your next feedback: the lists grow with the form, and only the form body scrolls.
- "Add input" / "Add output" scrolls to the new row and puts the cursor in its label.
