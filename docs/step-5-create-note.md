# Step 5. Create a Note with POST

## Goal

The goal of this step is to create a new note by sending data to the server.

So far, we have only used `GET` requests:

```text
GET /health
GET /hello
GET /notes
GET /notes/{note_id}
GET /notes?category=web
```

`GET` is used to read data.

In this step, we will create:

```text
POST /notes
```

`POST` is commonly used to create new data.

By the end of this step, you should be able to:

- Understand the difference between `GET` and `POST`
- Send JSON data to the server
- Use a Pydantic model to define the request body
- Create a new note from client input
- Add the new note to the in-memory notes list
- Test a POST endpoint using FastAPI `/docs`

---

## Before You Start

Make sure you completed Step 4.

Your `main.py` should currently have:

```python
from fastapi import FastAPI

app = FastAPI()

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

Before making changes, create a new branch for Step 5.

Make sure you are on the latest `main` branch:

```bash
git checkout main
git pull
```

Create a new branch:

```bash
git checkout -b step-5-create-note
```

This keeps your Step 5 work separate from the stable `main` branch.

---

# 2. Understand GET vs POST

So far, we used `GET`.

`GET` is used when the client wants to read data.

Examples:

```text
GET /notes
GET /notes/1
GET /notes?category=web
```

In this step, we will use `POST`.

`POST` is used when the client sends data to the server, usually to create something new.

Example:

```text
POST /notes
```

The client will send JSON data like this:

```json
{
  "title": "HTTP POST",
  "content": "POST is used when the client sends data to the server.",
  "category": "web"
}
```

The server will receive that data, create a new note, add an ID, and store it in the `notes` list.

---

# 3. Import BaseModel

In `main.py`, update the import section.

Change this:

```python
from fastapi import FastAPI
```

to this:

```python
from fastapi import FastAPI
from pydantic import BaseModel
```

`BaseModel` comes from Pydantic.

FastAPI uses Pydantic models to define and validate request data.

---

# 4. Create a Pydantic Model

Below this line:

```python
app = FastAPI()
```

add this class:

```python
class NoteCreate(BaseModel):
    title: str
    content: str
    category: str
```

This defines the shape of the data that the client must send when creating a note.

The client must send:

```text
title: string
content: string
category: string
```

For example:

```json
{
  "title": "HTTP POST",
  "content": "POST is used when the client sends data to the server.",
  "category": "web"
}
```

Notice that the client does not send an `id`.

The server will create the `id`.

---

# 5. Add the `POST /notes` Endpoint

Below the existing `GET /notes` endpoint, add this code:

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

This creates a new endpoint:

```text
POST /notes
```

When a client sends note data to this endpoint, the server will:

```text
Receive the JSON request body
Validate it using NoteCreate
Create a new note dictionary
Add a new id
Append the new note to the notes list
Return the created note as JSON
```

---

# 6. Full `main.py` After This Step

Your `main.py` should look like this:

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

Important: keep `GET /notes/{note_id}` after `GET /notes` and `POST /notes`.

---

# 7. Run the Server

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

# 8. Test Existing Endpoints First

Before testing the new POST endpoint, make sure the old endpoints still work.

Open:

```text
http://127.0.0.1:8000/health
http://127.0.0.1:8000/hello
http://127.0.0.1:8000/notes
http://127.0.0.1:8000/notes/1
http://127.0.0.1:8000/notes?category=web
```

These should still work.

---

# 9. Test `POST /notes` Using FastAPI Docs

You usually cannot test a `POST` request just by typing a URL into the browser address bar.

The browser address bar usually sends a `GET` request.

To test `POST /notes`, open FastAPI docs:

```text
http://127.0.0.1:8000/docs
```

Find:

```text
POST /notes
```

Click it.

Click **Try it out**.

You should see a request body box.

Enter this JSON:

```json
{
  "title": "HTTP POST",
  "content": "POST is used when the client sends data to the server.",
  "category": "web"
}
```

Click **Execute**.

You should see a response like this:

```json
{
  "id": 5,
  "title": "HTTP POST",
  "content": "POST is used when the client sends data to the server.",
  "category": "web"
}
```

The server added the `id`.

---

# 10. Confirm the New Note Was Added

After creating the note, test:

```text
GET /notes
```

In the `/docs` page, execute:

```text
GET /notes
```

Or open:

```text
http://127.0.0.1:8000/notes
```

You should see the new note in the list.

Also try:

```text
http://127.0.0.1:8000/notes/5
```

You should see the new note.

---

# 11. Test Input Validation

FastAPI uses the `NoteCreate` model to validate input.

Try sending an invalid request body.

For example, remove `title`:

```json
{
  "content": "This request is missing a title.",
  "category": "web"
}
```

Click **Execute**.

FastAPI should return a validation error.

This happens because `title` is required in the model:

```python
class NoteCreate(BaseModel):
    title: str
    content: str
    category: str
```

Now try sending a complete request again:

```json
{
  "title": "Validation",
  "content": "FastAPI checks that the request body has the required fields.",
  "category": "concept"
}
```

This should work.

---

# 12. Understand In-Memory Data

Right now, new notes are added to the Python list:

```python
notes.append(new_note)
```

This means the new note exists while the server is running.

However, the note is not saved to a file or database yet.

Try this:

1. Create a new note using `POST /notes`
2. Confirm it appears in `GET /notes`
3. Stop the server with `Ctrl + C`
4. Start the server again:

```bash
uv run uvicorn main:app --reload
```

5. Open:

```text
http://127.0.0.1:8000/notes
```

The note you created with `POST /notes` will be gone.

Why?

Because the data was only stored in memory.

When the server restarts, Python reloads the original hardcoded `notes` list from `main.py`.

This is an important backend concept.

```text
In-memory data disappears when the server restarts.
Persistent data stays after the server restarts.
```

In Step 6, we will save notes to a JSON file so the data can persist.

---

# 13. Understand How the ID Is Created

The new note ID is created with:

```python
"id": len(notes) + 1
```

This means:

```text
Count how many notes currently exist.
Add 1.
Use that as the new ID.
```

If there are 4 notes, the new ID is:

```text
5
```

This is simple and okay for now.

However, it is not perfect.

Later, if we delete notes or use a database, ID generation should be handled more carefully.

For now, this is enough for learning.

---

# 14. Common Problems

## Problem: `NameError: name 'BaseModel' is not defined`

Make sure you imported `BaseModel`:

```python
from pydantic import BaseModel
```

---

## Problem: `POST /notes` does not appear in `/docs`

Make sure you added this endpoint:

```python
@app.post("/notes")
def create_note(note: NoteCreate):
    ...
```

Also make sure the server restarted successfully.

---

## Problem: Validation error when sending JSON

Make sure your request body includes all required fields:

```json
{
  "title": "HTTP POST",
  "content": "POST is used when the client sends data to the server.",
  "category": "web"
}
```

All three fields are required:

```text
title
content
category
```

---

## Problem: New note disappears after restart

That is expected in this step.

The note is only stored in memory.

It is not saved to a file or database yet.

Step 6 will fix this by saving notes to a JSON file.

---

## Problem: `/notes/5` does not show the new note

Make sure you created the note first using `POST /notes`.

Then check `GET /notes` to confirm the new note exists.

Also remember: if you restarted the server, the created note disappeared.

---

# 15. Commit Your Changes

After testing that `POST /notes` works, commit your changes.

Check the changed files:

```bash
git status
```

Add the files:

```bash
git add main.py docs/step-5-create-note.md
```

Commit:

```bash
git commit -m "Add create note endpoint"
```

Push your branch:

```bash
git push -u origin step-5-create-note
```

---

# 16. Open a Pull Request

Open a pull request from:

```text
step-5-create-note
```

into:

```text
main
```

Use this PR title:

```text
Add create note endpoint
```

Use this PR description:

```markdown
## Summary

Added a `POST /notes` endpoint that creates a new note from a JSON request body.

## Changes

- Added `NoteCreate` Pydantic model
- Added `POST /notes`
- Added logic to generate a new note ID
- Added logic to append the new note to the in-memory notes list
- Confirmed that the new note appears in `GET /notes`

## How I tested it

I ran:

```bash
uv run uvicorn main:app --reload
```

Then I opened:

```text
http://127.0.0.1:8000/docs
```

I tested `POST /notes` with this request body:

```json
{
  "title": "HTTP POST",
  "content": "POST is used when the client sends data to the server.",
  "category": "web"
}
```

I also tested:

```text
GET /notes
GET /notes/5
GET /notes?category=web
```

I confirmed that the new note was added while the server was running.

I also restarted the server and observed that the new note disappeared because the data is still only stored in memory.

## What I learned

Write 2-3 sentences about what you learned.
```

---

# 17. Step 5 Completion Checklist

You are done with Step 5 if you completed the following:

```text
[ ] Created a new branch for Step 5
[ ] Imported BaseModel from pydantic
[ ] Created the NoteCreate model
[ ] Added POST /notes
[ ] Created a new note from the request body
[ ] Generated an ID for the new note
[ ] Appended the new note to the notes list
[ ] Tested POST /notes using /docs
[ ] Confirmed the new note appears in GET /notes
[ ] Confirmed the new note can be retrieved by ID
[ ] Tested validation by sending incomplete JSON
[ ] Restarted the server and observed that the new note disappeared
[ ] Committed the changes
[ ] Pushed the branch to GitHub
[ ] Opened a pull request
[ ] Wrote how you tested it in the PR description
[ ] Wrote 2-3 sentences about what you learned
```

---

# 18. Questions to Answer

Before moving to Step 6, make sure you can answer these questions:

```text
1. What is the difference between GET and POST?
2. Why can’t we easily test POST /notes from the browser address bar?
3. What is a request body?
4. What is JSON?
5. What does the NoteCreate model define?
6. Why does the client not send an id?
7. How does the server create the new id?
8. What does notes.append(new_note) do?
9. Why does the new note disappear after restarting the server?
10. What does it mean that the data is stored in memory?
11. What kind of validation does FastAPI perform automatically?
12. Why do we create a separate branch for Step 5?
```

---

# 19. Key Ideas

The most important ideas from this step are:

```text
GET is usually used to read data.

POST is usually used to create data.

A POST request can include a JSON request body.

FastAPI uses Pydantic models to define and validate request bodies.

The server can receive data from the client and create a new object.

The new note is stored in memory by appending it to the notes list.

In-memory data disappears when the server restarts.

Persistent storage is needed if we want data to survive server restarts.
```

---

# Next Step

In Step 6, we will save notes to a JSON file.

We will use:

```text
notes.json
```

This will help us understand the difference between in-memory data and persistent data.
