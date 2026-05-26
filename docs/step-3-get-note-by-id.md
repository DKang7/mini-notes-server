# Step 3. Get One Note by ID

## Goal

The goal of this step is to create an endpoint that returns one specific note by its ID.

In Step 2, we created:

```text
GET /notes
```

That endpoint returns all notes.

In this step, we will create:

```text
GET /notes/{note_id}
```

For example:

```text
GET /notes/1
GET /notes/2
GET /notes/100
```

By the end of this step, you should be able to:

- Use a path parameter in FastAPI
- Receive a value from the URL
- Search a Python list for one matching item
- Return one note as JSON
- Return an error when the note does not exist
- Test the endpoint using the browser and FastAPI `/docs`

---

## Before You Start

Make sure you completed Step 2.

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
def get_notes():
    return notes
```

Also make sure your server can run with:

```bash
uv run uvicorn main:app --reload
```

---

# 1. Create a New Branch

Before making changes, create a new branch for Step 3.

Make sure you are on the latest `main` branch:

```bash
git checkout main
git pull
```

Create a new branch:

```bash
git checkout -b step-3-get-note-by-id
```

This keeps your Step 3 work separate from the stable `main` branch.

---

# 2. Add the `GET /notes/{note_id}` Endpoint

Open `main.py`.

Below the existing `GET /notes` endpoint, add this code:

```python
@app.get("/notes/{note_id}")
def get_note(note_id: int):
    for note in notes:
        if note["id"] == note_id:
            return note

    return {"error": "Note not found"}
```

Your new endpoint is:

```text
GET /notes/{note_id}
```

The `{note_id}` part means FastAPI will take that part of the URL and pass it into the Python function.

For example:

```text
/notes/1  →  note_id = 1
/notes/2  →  note_id = 2
/notes/100  →  note_id = 100
```

---

# 3. Full `main.py` After This Step

Your `main.py` should look like this:

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
def get_notes():
    return notes


@app.get("/notes/{note_id}")
def get_note(note_id: int):
    for note in notes:
        if note["id"] == note_id:
            return note

    return {"error": "Note not found"}
```

Save the file.

---

# 4. Run the Server

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

# 5. Test Existing Endpoint First

Before testing the new endpoint, make sure the old endpoint still works.

Open:

```text
http://127.0.0.1:8000/notes
```

You should still see all notes.

This confirms that Step 2 functionality still works.

---

# 6. Test `GET /notes/{note_id}` in the Browser

Open:

```text
http://127.0.0.1:8000/notes/1
```

You should see only the note with `id` 1:

```json
{
  "id": 1,
  "title": "Learn FastAPI",
  "content": "FastAPI is a Python framework for building APIs.",
  "category": "study"
}
```

Try another one:

```text
http://127.0.0.1:8000/notes/2
```

You should see only the note with `id` 2.

Try a note that does not exist:

```text
http://127.0.0.1:8000/notes/100
```

You should see:

```json
{
  "error": "Note not found"
}
```

---

# 7. Test Invalid Input

Try this URL:

```text
http://127.0.0.1:8000/notes/abc
```

You should see an error response from FastAPI.

This happens because the function says:

```python
def get_note(note_id: int):
```

The `note_id` must be an integer.

FastAPI tries to convert the URL value into an integer.  
`abc` cannot be converted into an integer, so FastAPI returns a validation error.

This is useful because FastAPI automatically checks the input type for us.

---

# 8. Test the Endpoint Using FastAPI Docs

Open:

```text
http://127.0.0.1:8000/docs
```

You should now see:

```text
GET /health
GET /hello
GET /notes
GET /notes/{note_id}
```

Click:

```text
GET /notes/{note_id}
```

Click **Try it out**.

Enter:

```text
1
```

for `note_id`.

Click **Execute**.

You should see the note with `id` 1.

Then try:

```text
100
```

You should see:

```json
{
  "error": "Note not found"
}
```

---

# 9. Understand Path Parameters

A path parameter is a value that appears directly inside the URL path.

For example:

```text
/notes/1
```

Here, `1` is part of the path.

In FastAPI, we define it like this:

```python
@app.get("/notes/{note_id}")
def get_note(note_id: int):
    ...
```

The name inside the route:

```python
{note_id}
```

must match the function parameter name:

```python
def get_note(note_id: int):
```

So this works:

```python
@app.get("/notes/{note_id}")
def get_note(note_id: int):
    ...
```

But this would be confusing and should not be used:

```python
@app.get("/notes/{note_id}")
def get_note(id: int):
    ...
```

Because `{note_id}` and `id` do not match.

---

# 10. Understand the Search Logic

This part loops through all notes:

```python
for note in notes:
    if note["id"] == note_id:
        return note
```

It means:

```text
Look at each note in the notes list.
If the note's id matches note_id, return that note.
```

If no matching note is found, the function continues to the end and returns:

```python
return {"error": "Note not found"}
```

For now, this is okay because we only have a few notes.

Later, when using a database, we would ask the database to find the note instead of looping through a Python list.

---

# 11. Important Note About Error Responses

Right now, when a note is not found, we return:

```python
return {"error": "Note not found"}
```

This works, but it still returns a normal HTTP 200 response.

Later, we will learn a better way to return a proper `404 Not Found` response using FastAPI’s `HTTPException`.

For now, the goal is to understand the basic flow first:

```text
Receive ID from URL
Search notes list
Return matching note
Return error message if not found
```

---

# 12. Common Problems

## Problem: `/notes/1` returns all notes

Make sure you added a separate endpoint:

```python
@app.get("/notes/{note_id}")
def get_note(note_id: int):
    ...
```

Do not replace the existing `GET /notes` endpoint.

You should have both:

```python
@app.get("/notes")
def get_notes():
    return notes


@app.get("/notes/{note_id}")
def get_note(note_id: int):
    ...
```

---

## Problem: `NameError: name 'note_id' is not defined`

Make sure `note_id` is included in the function parameter:

```python
def get_note(note_id: int):
```

---

## Problem: `/notes/100` returns nothing

Make sure you included the final return statement:

```python
return {"error": "Note not found"}
```

This should be outside the `for` loop.

Correct:

```python
@app.get("/notes/{note_id}")
def get_note(note_id: int):
    for note in notes:
        if note["id"] == note_id:
            return note

    return {"error": "Note not found"}
```

Incorrect:

```python
@app.get("/notes/{note_id}")
def get_note(note_id: int):
    for note in notes:
        if note["id"] == note_id:
            return note
        return {"error": "Note not found"}
```

In the incorrect version, the function returns too early after checking only the first note.

---

## Problem: Browser still shows old result

Try refreshing the browser.

Also check the terminal. If there is a Python error, Uvicorn may not have restarted successfully.

If needed, stop the server:

```text
Ctrl + C
```

Then restart it:

```bash
uv run uvicorn main:app --reload
```

---

# 13. Commit Your Changes

After testing that `/notes/{note_id}` works, commit your changes.

Check the changed files:

```bash
git status
```

Add the files:

```bash
git add main.py docs/step-3-get-note-by-id.md
```

Commit:

```bash
git commit -m "Add note detail endpoint"
```

Push your branch:

```bash
git push -u origin step-3-get-note-by-id
```

---

# 14. Open a Pull Request

Open a pull request from:

```text
step-3-get-note-by-id
```

into:

```text
main
```

Use this PR title:

```text
Add note detail endpoint
```

Use this PR description:

```markdown
## Summary

Added a `GET /notes/{note_id}` endpoint that returns one note by ID.

## Changes

- Added a path parameter endpoint for note ID
- Added logic to search the notes list
- Added a simple error response when the note is not found
- Tested valid, missing, and invalid note IDs

## How I tested it

I ran:

```bash
uv run uvicorn main:app --reload
```

Then I opened:

```text
http://127.0.0.1:8000/notes
http://127.0.0.1:8000/notes/1
http://127.0.0.1:8000/notes/2
http://127.0.0.1:8000/notes/100
http://127.0.0.1:8000/notes/abc
http://127.0.0.1:8000/docs
```

I confirmed that valid note IDs return one note, missing IDs return an error message, and invalid IDs return a FastAPI validation error.

## What I learned

Write 2-3 sentences about what you learned.
```

---

# 15. Step 3 Completion Checklist

You are done with Step 3 if you completed the following:

```text
[ ] Created a new branch for Step 3
[ ] Added GET /notes/{note_id}
[ ] Used note_id as a path parameter
[ ] Searched the notes list for a matching ID
[ ] Returned one note when the ID exists
[ ] Returned an error message when the ID does not exist
[ ] Tested /notes/1 in the browser
[ ] Tested /notes/100 in the browser
[ ] Tested /notes/abc in the browser
[ ] Tested the endpoint using /docs
[ ] Committed the changes
[ ] Pushed the branch to GitHub
[ ] Opened a pull request
[ ] Wrote how you tested it in the PR description
[ ] Wrote 2-3 sentences about what you learned
```

---

# 16. Questions to Answer

Before moving to Step 4, make sure you can answer these questions:

```text
1. What is a path parameter?
2. In /notes/1, what is the path parameter value?
3. Why does note_id need to be in both the route and the function parameter?
4. Why do we write note_id: int instead of just note_id?
5. What happens when you visit /notes/abc?
6. How does the server find the matching note?
7. What happens if no note matches the given ID?
8. Why should the error response eventually be changed to a proper 404?
9. What is the difference between GET /notes and GET /notes/{note_id}?
10. Why do we create a separate branch for Step 3?
```

---

# 17. Key Ideas

The most important ideas from this step are:

```text
A path parameter is a value inside the URL path.

FastAPI passes path parameter values into Python function parameters.

Type hints such as int allow FastAPI to validate and convert input.

GET /notes returns all notes.

GET /notes/{note_id} returns one note.

The server can use input from the URL to decide what data to return.

A branch and pull request help keep each step organized and reviewable.
```

---

# Next Step

In Step 4, we will filter notes using query parameters.

We will create:

```text
GET /notes?category=web
GET /notes?category=study
```

This will help us understand the difference between path parameters and query parameters.
