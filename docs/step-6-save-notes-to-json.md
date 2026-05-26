# Step 6. Save Notes to a JSON File

## Goal

The goal of this step is to save notes to a JSON file so that created notes do not disappear after restarting the server.

In Step 5, we created:

```text
POST /notes
```

This allowed the client to create a new note.

However, the new note was only stored in memory:

```python
notes.append(new_note)
```

That means the new note disappeared when the server restarted.

In this step, we will use a file:

```text
notes.json
```

By the end of this step, you should be able to:

- Understand the difference between in-memory data and persistent data
- Read data from a JSON file
- Write data to a JSON file
- Load notes when the server starts
- Save notes when a new note is created
- Confirm that created notes still exist after restarting the server

---

## Before You Start

Make sure you completed Step 5.

Your `main.py` should currently look something like this:

```python
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class NoteCreate(BaseModel):
    title: str
    content: str
    category: str


notes = [
    {
        "id": 1,
        "title": "Learn FastAPI",
        "content": "FastAPI is a Python framework for building APIs.",
        "category": "study",
    },
    {
        "id": 2,
        "title": "What is a server?",
        "content": "A server is a program that waits for requests and sends responses.",
        "category": "concept",
    },
    {
        "id": 3,
        "title": "HTTP GET",
        "content": "GET is used when the client wants to read data from the server.",
        "category": "web",
    },
    {
        "id": 4,
        "title": "API Response",
        "content": "An API response is the data sent back from the server to the client.",
        "category": "web",
    },
]


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/hello")
def hello():
    return {"message": "Hello, FastAPI!"}


@app.get("/notes")
def get_notes(category: str | None = None):
    if category is None:
        return notes

    filtered_notes = []

    for note in notes:
        if note["category"] == category:
            filtered_notes.append(note)

    return filtered_notes


@app.post("/notes")
def create_note(note: NoteCreate):
    new_note = {
        "id": len(notes) + 1,
        "title": note.title,
        "content": note.content,
        "category": note.category,
    }

    notes.append(new_note)

    return new_note


@app.get("/notes/{note_id}")
def get_note(note_id: int):
    for note in notes:
        if note["id"] == note_id:
            return note

    return {"error": "Note not found"}
```

Also make sure your server can run with:

```bash
uv run uvicorn main:app --reload
```

---

# 1. Create a New Branch

Before making changes, create a new branch for Step 6.

Make sure you are on the latest `main` branch:

```bash
git checkout main
git pull
```

Create a new branch:

```bash
git checkout -b step-6-save-notes-to-json
```

This keeps your Step 6 work separate from the stable `main` branch.

---

# 2. Understand the Problem

Right now, the notes are stored directly in Python memory.

The original notes are hardcoded in `main.py`:

```python
notes = [
    {
        "id": 1,
        "title": "Learn FastAPI",
        "content": "FastAPI is a Python framework for building APIs.",
        "category": "study",
    }
]
```

When the server is running and we call:

```text
POST /notes
```

the new note is added to the Python list:

```python
notes.append(new_note)
```

But this list only exists while the Python program is running.

When the server restarts:

```text
Python starts again
main.py is loaded again
the original hardcoded notes list is recreated
the POST-created notes are gone
```

To fix this, we will store the notes in a file.

---

# 3. Create `notes.json`

Create a new file in the project root:

```text
notes.json
```

Your project should look like this:

```text
mini-notes-server/
  README.md
  main.py
  notes.json
  pyproject.toml
  uv.lock
  docs/
    step-1-hello-fastapi-server.md
    step-2-get-notes.md
    step-3-get-note-by-id.md
    step-4-filter-notes.md
    step-5-create-note.md
    step-6-save-notes-to-json.md
```

Add this content to `notes.json`:

```json
[
  {
    "id": 1,
    "title": "Learn FastAPI",
    "content": "FastAPI is a Python framework for building APIs.",
    "category": "study"
  },
  {
    "id": 2,
    "title": "What is a server?",
    "content": "A server is a program that waits for requests and sends responses.",
    "category": "concept"
  },
  {
    "id": 3,
    "title": "HTTP GET",
    "content": "GET is used when the client wants to read data from the server.",
    "category": "web"
  },
  {
    "id": 4,
    "title": "API Response",
    "content": "An API response is the data sent back from the server to the client.",
    "category": "web"
  }
]
```

This file will become the source of truth for our notes data.

---

# 4. Import `json` and `Path`

In `main.py`, add two imports at the top.

Change this:

```python
from fastapi import FastAPI
from pydantic import BaseModel
```

to this:

```python
import json
from pathlib import Path

from fastapi import FastAPI
from pydantic import BaseModel
```

We use:

```python
json
```

to read and write JSON data.

We use:

```python
Path
```

to represent the path to the `notes.json` file.

---

# 5. Add the File Path

Below this line:

```python
app = FastAPI()
```

add:

```python
NOTES_FILE = Path("notes.json")
```

This gives us one place to define where the notes file is located.

---

# 6. Add a Function to Load Notes

Below the `NoteCreate` class, add this function:

```python
def load_notes():
    with open(NOTES_FILE, "r") as file:
        return json.load(file)
```

This function opens `notes.json`, reads the JSON content, and converts it into Python data.

The JSON file contains a list of note objects.

After loading, Python sees it as a list of dictionaries.

---

# 7. Add a Function to Save Notes

Below `load_notes()`, add this function:

```python
def save_notes():
    with open(NOTES_FILE, "w") as file:
        json.dump(notes, file, indent=2)
```

This function takes the current `notes` list and writes it back to `notes.json`.

The `indent=2` part makes the file easier for humans to read.

---

# 8. Replace the Hardcoded Notes List

Find the hardcoded `notes = [...]` list in `main.py`.

Remove the whole list and replace it with:

```python
notes = load_notes()
```

This means:

```text
When the server starts,
read notes.json,
load the notes into memory,
and store them in the notes variable.
```

Now the notes data comes from the file instead of being hardcoded in the Python code.

---

# 9. Update `POST /notes` to Save to File

Find the `POST /notes` endpoint:

```python
@app.post("/notes")
def create_note(note: NoteCreate):
    new_note = {
        "id": len(notes) + 1,
        "title": note.title,
        "content": note.content,
        "category": note.category,
    }

    notes.append(new_note)

    return new_note
```

Update it to call `save_notes()` after appending the new note:

```python
@app.post("/notes")
def create_note(note: NoteCreate):
    new_note = {
        "id": len(notes) + 1,
        "title": note.title,
        "content": note.content,
        "category": note.category,
    }

    notes.append(new_note)
    save_notes()

    return new_note
```

Now, whenever a new note is created, the server updates both:

```text
memory
notes.json file
```

---

# 10. Full `main.py` After This Step

Your `main.py` should look like this:

```python
import json
from pathlib import Path

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

NOTES_FILE = Path("notes.json")


class NoteCreate(BaseModel):
    title: str
    content: str
    category: str


def load_notes():
    with open(NOTES_FILE, "r") as file:
        return json.load(file)


def save_notes():
    with open(NOTES_FILE, "w") as file:
        json.dump(notes, file, indent=2)


notes = load_notes()


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/hello")
def hello():
    return {"message": "Hello, FastAPI!"}


@app.get("/notes")
def get_notes(category: str | None = None):
    if category is None:
        return notes

    filtered_notes = []

    for note in notes:
        if note["category"] == category:
            filtered_notes.append(note)

    return filtered_notes


@app.post("/notes")
def create_note(note: NoteCreate):
    new_note = {
        "id": len(notes) + 1,
        "title": note.title,
        "content": note.content,
        "category": note.category,
    }

    notes.append(new_note)
    save_notes()

    return new_note


@app.get("/notes/{note_id}")
def get_note(note_id: int):
    for note in notes:
        if note["id"] == note_id:
            return note

    return {"error": "Note not found"}
```

Save the file.

---

# 11. Run the Server

Run the server:

```bash
uv run uvicorn main:app --reload
```

You should see output similar to this:

```text
INFO:     Uvicorn running on http://127.0.0.1:8000
INFO:     Application startup complete.
```

---

# 12. Test Existing Endpoints First

Before testing persistence, make sure existing endpoints still work.

Open:

```text
http://127.0.0.1:8000/health
http://127.0.0.1:8000/hello
http://127.0.0.1:8000/notes
http://127.0.0.1:8000/notes/1
http://127.0.0.1:8000/notes?category=web
```

Everything should still work.

---

# 13. Create a New Note

Open FastAPI docs:

```text
http://127.0.0.1:8000/docs
```

Find:

```text
POST /notes
```

Click **Try it out**.

Use this request body:

```json
{
  "title": "Persistent Storage",
  "content": "Persistent storage keeps data even after the server restarts.",
  "category": "concept"
}
```

Click **Execute**.

You should see a response like this:

```json
{
  "id": 5,
  "title": "Persistent Storage",
  "content": "Persistent storage keeps data even after the server restarts.",
  "category": "concept"
}
```

---

# 14. Check `notes.json`

Open `notes.json` in VS Code.

You should see that the new note was added to the file.

This is the key difference from Step 5.

In Step 5:

```text
POST /notes changed memory only.
```

In Step 6:

```text
POST /notes changes memory and notes.json.
```

---

# 15. Restart the Server and Confirm Persistence

Stop the server:

```text
Ctrl + C
```

Start it again:

```bash
uv run uvicorn main:app --reload
```

Open:

```text
http://127.0.0.1:8000/notes
```

You should still see the note you created.

This proves that the data is now persistent.

---

# 16. Test `GET /notes/{note_id}` with the New Note

If the new note has ID 5, open:

```text
http://127.0.0.1:8000/notes/5
```

You should see:

```json
{
  "id": 5,
  "title": "Persistent Storage",
  "content": "Persistent storage keeps data even after the server restarts.",
  "category": "concept"
}
```

If your note has a different ID, use that ID.

---

# 17. Understand Persistent Storage

In-memory storage:

```text
Data is stored in Python memory.
Fast and simple.
Disappears when the server restarts.
```

File storage:

```text
Data is written to a file.
Survives server restarts.
Still simple enough for learning.
Not ideal for larger real-world apps.
```

Database storage:

```text
Data is stored in a database.
Better for real applications.
Supports stronger querying, updating, deleting, and concurrent access.
```

In this project, `notes.json` is a stepping stone.

It helps us understand persistence before moving to a real database.

---

# 18. Important Limitation

This JSON file approach is simple, but it is not perfect.

For example:

```text
If two users create notes at the exact same time,
file writes could conflict.

If the file becomes very large,
reading and writing the whole file becomes inefficient.

If the JSON file is accidentally broken,
the server may fail to start.
```

That is why real backend applications usually use databases.

But for this learning project, JSON file storage is a good next step.

---

# 19. Common Problems

## Problem: `FileNotFoundError: notes.json`

Make sure `notes.json` exists in the project root.

It should be next to `main.py`:

```text
mini-notes-server/
  main.py
  notes.json
```

---

## Problem: `JSONDecodeError`

This means `notes.json` contains invalid JSON.

Common JSON mistakes:

```text
Missing comma
Extra comma at the end
Using single quotes instead of double quotes
Missing closing bracket
```

Valid JSON uses double quotes:

```json
{
  "title": "Example"
}
```

Invalid JSON:

```json
{
  'title': 'Example'
}
```

---

## Problem: New note is created but not saved

Make sure `save_notes()` is called after `notes.append(new_note)`:

```python
notes.append(new_note)
save_notes()
```

---

## Problem: Server keeps restarting when saving notes

Because the server runs with `--reload`, it watches files for changes.

Depending on your environment, changing `notes.json` may cause the server to reload.

That is okay for now.

In larger projects, we may configure which folders/files the server watches.

---

## Problem: ID numbers are repeated or unexpected

This can happen if notes were manually edited in `notes.json`.

For now, we use:

```python
"id": len(notes) + 1
```

This is simple, but not perfect.

A database would handle ID generation better.

---

# 20. Commit Your Changes

After testing that persistence works, commit your changes.

Check the changed files:

```bash
git status
```

Add the files:

```bash
git add main.py notes.json docs/step-6-save-notes-to-json.md
```

Commit:

```bash
git commit -m "Save notes to JSON file"
```

Push your branch:

```bash
git push -u origin step-6-save-notes-to-json
```

---

# 21. Open a Pull Request

Open a pull request from:

```text
step-6-save-notes-to-json
```

into:

```text
main
```

Use this PR title:

```text
Save notes to JSON file
```

Use this PR description:

```markdown
## Summary

Updated the notes API so notes are loaded from and saved to a JSON file.

## Changes

- Added `notes.json`
- Added `load_notes()` to read notes from the JSON file
- Added `save_notes()` to write notes to the JSON file
- Updated the app to load notes when the server starts
- Updated `POST /notes` to save new notes to the JSON file

## How I tested it

I ran:

```bash
uv run uvicorn main:app --reload
```

Then I opened:

```text
http://127.0.0.1:8000/notes
http://127.0.0.1:8000/docs
```

I created a new note using `POST /notes`:

```json
{
  "title": "Persistent Storage",
  "content": "Persistent storage keeps data even after the server restarts.",
  "category": "concept"
}
```

Then I confirmed:

```text
- The new note appeared in GET /notes
- The new note was written to notes.json
- The note was still there after restarting the server
```

## What I learned

Write 2-3 sentences about what you learned.
```

---

# 22. Step 6 Completion Checklist

You are done with Step 6 if you completed the following:

```text
[ ] Created a new branch for Step 6
[ ] Created notes.json
[ ] Added initial notes to notes.json
[ ] Imported json and Path
[ ] Added NOTES_FILE = Path("notes.json")
[ ] Added load_notes()
[ ] Added save_notes()
[ ] Replaced the hardcoded notes list with notes = load_notes()
[ ] Updated POST /notes to call save_notes()
[ ] Ran the server using uv run uvicorn
[ ] Confirmed GET /notes still works
[ ] Created a new note using POST /notes
[ ] Confirmed the new note appears in notes.json
[ ] Restarted the server
[ ] Confirmed the new note still exists after restart
[ ] Committed the changes
[ ] Pushed the branch to GitHub
[ ] Opened a pull request
[ ] Wrote how you tested it in the PR description
[ ] Wrote 2-3 sentences about what you learned
```

---

# 23. Questions to Answer

Before finishing this learning module, make sure you can answer these questions:

```text
1. What is the difference between in-memory storage and persistent storage?
2. Why did POST-created notes disappear in Step 5?
3. What is notes.json used for?
4. What does json.load(file) do?
5. What does json.dump(notes, file, indent=2) do?
6. When does load_notes() run?
7. When does save_notes() run?
8. Why does the new note remain after restarting the server?
9. What are some limitations of using a JSON file as storage?
10. Why do real applications usually use a database?
11. Why is len(notes) + 1 simple but not perfect for generating IDs?
12. Why do we create a separate branch for Step 6?
```

---

# 24. Key Ideas

The most important ideas from this step are:

```text
In-memory data disappears when the server restarts.

Persistent data is stored outside the running program.

A JSON file can be used as simple persistent storage.

json.load() reads JSON from a file and converts it into Python data.

json.dump() writes Python data to a file as JSON.

The server can load data when it starts.

The server can save data when something changes.

File storage is useful for learning, but databases are better for real applications.
```

---

# Module Complete

You have now completed the first backend learning module.

You built a simple FastAPI notes server with:

```text
GET /health
GET /hello
GET /notes
GET /notes?category=web
GET /notes/{note_id}
POST /notes
```

You also learned:

```text
server basics
API endpoints
GET requests
POST requests
path parameters
query parameters
request bodies
Pydantic models
JSON responses
in-memory storage
persistent file storage
branch and PR workflow
```

A good next module would be one of these:

```text
Option 1: Improve API correctness with HTTP status codes and HTTPException
Option 2: Add update and delete endpoints
Option 3: Move from notes.json to SQLite
Option 4: Build a tiny frontend that calls this API
```
