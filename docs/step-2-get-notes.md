# Step 2. Return a List of Notes

## Goal

The goal of this step is to create a simple API endpoint that returns a list of notes.

In Step 1, we created two simple endpoints:

```text
GET /health
GET /hello
```

In this step, we will create:

```text
GET /notes
```

This endpoint will return a list of notes as JSON.

By the end of this step, you should be able to:

- Store simple data in a Python list
- Return a list of dictionaries as JSON
- Understand how a backend API can provide data to a client
- Test the endpoint in the browser
- Test the endpoint using FastAPI’s `/docs` page

---

## Before You Start

Make sure you completed Step 1.

Your `main.py` should currently look something like this:

```python
from fastapi import FastAPI

app = FastAPI()


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/hello")
def hello():
    return {"message": "Hello, FastAPI!"}
```

Also make sure your server can run with:

```bash
uv run uvicorn main:app --reload
```

---

# 1. Create a New Branch

Before making changes, create a new branch for Step 2.

Make sure you are on the latest `main` branch:

```bash
git checkout main
git pull
```

Create a new branch:

```bash
git checkout -b step-2-get-notes
```

This keeps your Step 2 work separate from the stable `main` branch.

---

# 2. Add Sample Notes Data

Open `main.py`.

Below this line:

```python
app = FastAPI()
```

add a Python list named `notes`:

```python
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
]
```

This is temporary sample data.

We are not using a database yet.  
For now, the notes are stored directly in memory as a Python list.

---

# 3. Create the `GET /notes` Endpoint

Below the existing `/hello` endpoint, add this code:

```python
@app.get("/notes")
def get_notes():
    return notes
```

This creates a new endpoint:

```text
GET /notes
```

When a client requests `/notes`, FastAPI will run the `get_notes()` function and return the `notes` list as JSON.

---

# 4. Full `main.py` After This Step

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

Save the file.

---

# 5. Run the Server

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

# 6. Test `GET /notes` in the Browser

Open your browser and go to:

```text
http://127.0.0.1:8000/notes
```

You should see a JSON response similar to this:

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
  }
]
```

This means the server successfully returned a list of notes.

---

# 7. Test the Endpoint Using FastAPI Docs

Open:

```text
http://127.0.0.1:8000/docs
```

You should now see three endpoints:

```text
GET /health
GET /hello
GET /notes
```

Click `GET /notes`.

Click **Try it out**.

Click **Execute**.

You should see the same list of notes in the response body.

---

# 8. Understand What Happened

In this step, the server returned a list of notes.

The data started as a Python list:

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

Then the endpoint returned that list:

```python
@app.get("/notes")
def get_notes():
    return notes
```

FastAPI automatically converted the Python list and dictionaries into JSON.

So this Python data:

```python
[
    {"id": 1, "title": "Learn FastAPI"}
]
```

became this JSON response:

```json
[
  {
    "id": 1,
    "title": "Learn FastAPI"
  }
]
```

This is one of the most common jobs of a backend API:

```text
Store or retrieve data
→ Convert it into a response format
→ Send it back to the client
```

---

# 9. What Does “In Memory” Mean?

Right now, the notes are stored in memory.

That means the data exists only while the Python server program is running.

The notes are defined directly inside `main.py`:

```python
notes = [...]
```

If you change this list in the code, the response from `/notes` changes.

But this is not a database.

For now:

```text
The data is hardcoded in the Python file.
The data is loaded when the server starts.
The data is not saved to a database.
```

Later, we will learn how to create new notes using `POST /notes`.

After that, we will learn why data disappears when the server restarts and how to save it to a file or database.

---

# 10. Add One More Note

Add one more note to the `notes` list.

For example:

```python
{
    "id": 4,
    "title": "API Response",
    "content": "An API response is the data sent back from the server to the client.",
    "category": "web",
}
```

Your list should now have four notes.

Save the file.

Because the server is running with `--reload`, it should restart automatically.

Refresh:

```text
http://127.0.0.1:8000/notes
```

You should see four notes.

---

# 11. Common Problems

## Problem: `/notes` returns “Not Found”

Check that you added this code:

```python
@app.get("/notes")
def get_notes():
    return notes
```

Also make sure the server restarted after saving the file.

---

## Problem: Python error about `notes` not defined

Make sure the `notes` list is defined before the `get_notes()` function.

For example, this is correct:

```python
notes = [...]

@app.get("/notes")
def get_notes():
    return notes
```

This may cause an error if `notes` does not exist yet:

```python
@app.get("/notes")
def get_notes():
    return notes
```

---

## Problem: SyntaxError

Check for missing commas between note objects.

Each dictionary in the list should be separated by a comma:

```python
notes = [
    {
        "id": 1,
        "title": "Learn FastAPI",
    },
    {
        "id": 2,
        "title": "What is a server?",
    },
]
```

Also check that brackets and braces match:

```text
[ ] for lists
{ } for dictionaries
```

---

## Problem: Browser still shows the old response

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

# 12. Commit Your Changes

After testing that `/notes` works, commit your changes.

Check the changed files:

```bash
git status
```

Add the files:

```bash
git add main.py docs/step-2-get-notes.md
```

Commit:

```bash
git commit -m "Add notes endpoint"
```

Push your branch:

```bash
git push -u origin step-2-get-notes
```

---

# 13. Open a Pull Request

Open a pull request from:

```text
step-2-get-notes
```

into:

```text
main
```

Use this PR title:

```text
Add notes endpoint
```

Use this PR description:

```markdown
## Summary

Added a `GET /notes` endpoint that returns a list of sample notes.

## Changes

- Added a hardcoded `notes` list in `main.py`
- Added `GET /notes`
- Tested the endpoint in the browser
- Tested the endpoint using FastAPI `/docs`

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

I confirmed that `/notes` returns a JSON list of notes.

## What I learned

Write 2-3 sentences about what you learned.
```

---

# 14. Step 2 Completion Checklist

You are done with Step 2 if you completed the following:

```text
[ ] Created a new branch for Step 2
[ ] Added a hardcoded notes list in main.py
[ ] Created GET /notes endpoint
[ ] Ran the server using uv run uvicorn
[ ] Opened /notes in the browser
[ ] Tested /notes using /docs
[ ] Added one more note and confirmed the response changed
[ ] Committed the changes
[ ] Pushed the branch to GitHub
[ ] Opened a pull request
[ ] Wrote how you tested it in the PR description
[ ] Wrote 2-3 sentences about what you learned
```

---

# 15. Questions to Answer

Before moving to Step 3, make sure you can answer these questions:

```text
1. What is the purpose of the notes list?
2. Is the notes list stored in a database?
3. What does GET /notes return?
4. What kind of data structure is notes in Python?
5. What format does the browser receive?
6. What does FastAPI do when you return a Python list?
7. What does “in memory” mean?
8. Why is hardcoded sample data useful at the beginning?
9. What would happen if you remove one note from the list and refresh /notes?
10. Why do we create a separate branch for Step 2?
```

---

# 16. Key Ideas

The most important ideas from this step are:

```text
A backend server often returns data to a client.

In FastAPI, returning a Python dictionary or list automatically produces a JSON response.

A list of dictionaries in Python is a simple way to represent multiple records.

The current notes data is hardcoded in main.py.

This data is in memory, not in a database.

GET /notes is an endpoint for reading data.

A branch and pull request help keep changes organized and reviewable.
```

---

# Next Step

In Step 3, we will create an endpoint that returns one specific note by ID.

We will create:

```text
GET /notes/{note_id}
```

For example:

```text
GET /notes/1
GET /notes/2
GET /notes/100
```

This will help us understand path parameters.
