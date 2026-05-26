# Step 4. Filter Notes with Query Parameters

## Goal

The goal of this step is to update the `GET /notes` endpoint so it can optionally filter notes by category.

In Step 2, we created:

```text
GET /notes
```

In Step 3, we created:

```text
GET /notes/{note_id}
```

In this step, we will support:

```text
GET /notes?category=web
GET /notes?category=study
GET /notes?category=concept
```

By the end of this step, you should be able to:

- Understand what a query parameter is
- Use optional query parameters in FastAPI
- Filter a Python list based on a condition
- Understand the difference between path parameters and query parameters
- Test query parameters in the browser and FastAPI `/docs`

---

## Before You Start

Make sure you completed Step 3.

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

Before making changes, create a new branch for Step 4.

Make sure you are on the latest `main` branch:

```bash
git checkout main
git pull
```

Create a new branch:

```bash
git checkout -b step-4-filter-notes
```

This keeps your Step 4 work separate from the stable `main` branch.

---

# 2. Understand Query Parameters

A query parameter is extra information added to the end of a URL after a question mark.

For example:

```text
/notes?category=web
```

In this URL:

```text
/notes
```

is the path.

```text
category=web
```

is the query parameter.

The `?` separates the path from the query parameter.

A query parameter usually means:

```text
Return the same kind of resource, but with some filter or option applied.
```

For this project:

```text
GET /notes
```

means:

```text
Return all notes.
```

But:

```text
GET /notes?category=web
```

means:

```text
Return only notes where category is web.
```

---

# 3. Update the `GET /notes` Endpoint

In `main.py`, find the current `GET /notes` endpoint:

```python
@app.get("/notes")
def get_notes():
    return notes
```

Replace it with this:

```python
@app.get("/notes")
def get_notes(category: str | None = None):
    if category is None:
        return notes

    filtered_notes = []

    for note in notes:
        if note["category"] == category:
            filtered_notes.append(note)

    return filtered_notes
```

Save the file.

---

# 4. Understand the Updated Code

The function now accepts an optional parameter:

```python
def get_notes(category: str | None = None):
```

This means:

```text
category can be a string,
or category can be None,
and if the client does not provide it,
the default value is None.
```

When the client calls:

```text
GET /notes
```

then:

```python
category = None
```

So this part runs:

```python
if category is None:
    return notes
```

The server returns all notes.

When the client calls:

```text
GET /notes?category=web
```

then:

```python
category = "web"
```

So the function filters the notes list and returns only matching notes.

---

# 5. Full `main.py` After This Step

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

---

# 6. Run the Server

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

# 7. Test Without Query Parameter

Open:

```text
http://127.0.0.1:8000/notes
```

You should see all notes.

This confirms that the endpoint still works without a filter.

---

# 8. Test with Category Filters

Open:

```text
http://127.0.0.1:8000/notes?category=web
```

You should see only notes where:

```json
"category": "web"
```

You should see two notes:

```json
[
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

Now test:

```text
http://127.0.0.1:8000/notes?category=study
```

You should see only study notes.

Test:

```text
http://127.0.0.1:8000/notes?category=concept
```

You should see only concept notes.

---

# 9. Test a Category That Does Not Exist

Open:

```text
http://127.0.0.1:8000/notes?category=random
```

You should see:

```json
[]
```

This is an empty list.

It means:

```text
The request was valid,
but no notes matched the filter.
```

This is different from an error.

---

# 10. Test Existing Detail Endpoint

Make sure Step 3 still works.

Open:

```text
http://127.0.0.1:8000/notes/1
```

You should still see the note with ID 1.

This confirms that your new query parameter feature did not break the existing path parameter endpoint.

---

# 11. Test the Endpoint Using FastAPI Docs

Open:

```text
http://127.0.0.1:8000/docs
```

Click:

```text
GET /notes
```

Click **Try it out**.

You should see a field for:

```text
category
```

Try leaving it blank and click **Execute**.

You should see all notes.

Then try entering:

```text
web
```

Click **Execute**.

You should see only web notes.

---

# 12. Path Parameters vs Query Parameters

You have now used both path parameters and query parameters.

## Path parameter

Example:

```text
GET /notes/1
```

This means:

```text
Get the specific note whose ID is 1.
```

The ID is part of the path.

In FastAPI:

```python
@app.get("/notes/{note_id}")
def get_note(note_id: int):
    ...
```

## Query parameter

Example:

```text
GET /notes?category=web
```

This means:

```text
Get notes, but filter them by category.
```

The category is added after the `?`.

In FastAPI:

```python
@app.get("/notes")
def get_notes(category: str | None = None):
    ...
```

## Simple rule of thumb

Use a path parameter when you are identifying a specific resource:

```text
/notes/1
/users/5
/orders/100
```

Use a query parameter when you are filtering, sorting, or changing how a list is returned:

```text
/notes?category=web
/users?role=admin
/orders?status=pending
```

---

# 13. Common Problems

## Problem: `/notes?category=web` returns all notes

Check that your `get_notes` function has the `category` parameter:

```python
def get_notes(category: str | None = None):
```

Also make sure you replaced the old function:

```python
def get_notes():
    return notes
```

---

## Problem: `/notes` no longer works

Make sure the parameter has a default value:

```python
category: str | None = None
```

If you write this:

```python
def get_notes(category: str):
```

then FastAPI treats `category` as required.

For this step, `category` should be optional.

---

## Problem: `/notes?category=Web` returns an empty list

This is because string comparison is case-sensitive.

The category in the data is:

```text
web
```

But the query used:

```text
Web
```

For now, use lowercase category names.

Later, we could make the comparison case-insensitive.

---

## Problem: `/notes/1` stopped working

Make sure both endpoints still exist:

```python
@app.get("/notes")
def get_notes(category: str | None = None):
    ...


@app.get("/notes/{note_id}")
def get_note(note_id: int):
    ...
```

The list endpoint and detail endpoint are separate.

---

# 14. Commit Your Changes

After testing that the filter works, commit your changes.

Check the changed files:

```bash
git status
```

Add the files:

```bash
git add main.py docs/step-4-filter-notes.md
```

Commit:

```bash
git commit -m "Add category filter for notes"
```

Push your branch:

```bash
git push -u origin step-4-filter-notes
```

---

# 15. Open a Pull Request

Open a pull request from:

```text
step-4-filter-notes
```

into:

```text
main
```

Use this PR title:

```text
Add category filter for notes
```

Use this PR description:

```markdown
## Summary

Updated `GET /notes` to support filtering by category using a query parameter.

## Changes

- Added optional `category` query parameter to `GET /notes`
- Added filtering logic for the notes list
- Confirmed `GET /notes` still returns all notes when no category is provided
- Confirmed `GET /notes/{note_id}` still works

## How I tested it

I ran:

```bash
uv run uvicorn main:app --reload
```

Then I opened:

```text
http://127.0.0.1:8000/notes
http://127.0.0.1:8000/notes?category=web
http://127.0.0.1:8000/notes?category=study
http://127.0.0.1:8000/notes?category=concept
http://127.0.0.1:8000/notes?category=random
http://127.0.0.1:8000/notes/1
http://127.0.0.1:8000/docs
```

I confirmed that the category filter works and existing endpoints still work.

## What I learned

Write 2-3 sentences about what you learned.
```

---

# 16. Step 4 Completion Checklist

You are done with Step 4 if you completed the following:

```text
[ ] Created a new branch for Step 4
[ ] Updated GET /notes to accept an optional category query parameter
[ ] Returned all notes when category is not provided
[ ] Returned filtered notes when category is provided
[ ] Tested /notes in the browser
[ ] Tested /notes?category=web in the browser
[ ] Tested /notes?category=random in the browser
[ ] Confirmed /notes/{note_id} still works
[ ] Tested the query parameter using /docs
[ ] Committed the changes
[ ] Pushed the branch to GitHub
[ ] Opened a pull request
[ ] Wrote how you tested it in the PR description
[ ] Wrote 2-3 sentences about what you learned
```

---

# 17. Questions to Answer

Before moving to Step 5, make sure you can answer these questions:

```text
1. What is a query parameter?
2. In /notes?category=web, what is the query parameter?
3. What is the difference between /notes/1 and /notes?category=web?
4. Why is category optional in this step?
5. What happens when category is not provided?
6. What happens when category is provided?
7. Why does /notes?category=random return an empty list instead of an error?
8. Why is /notes/1 better as a path parameter instead of a query parameter?
9. When would you use a query parameter in a real API?
10. Why should we test old endpoints after adding a new feature?
```

---

# 18. Key Ideas

The most important ideas from this step are:

```text
A query parameter is extra information added after ? in a URL.

Query parameters are often used for filtering, sorting, searching, or pagination.

FastAPI automatically passes query parameter values into function parameters.

An optional query parameter should have a default value.

GET /notes returns all notes.

GET /notes?category=web returns filtered notes.

Path parameters identify a specific resource.

Query parameters modify or filter a request.

After adding a new feature, existing features should still be tested.
```

---

# Next Step

In Step 5, we will create a note using a POST request.

We will create:

```text
POST /notes
```

This will help us understand request bodies, JSON input, and Pydantic models.
