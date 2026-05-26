# Mini Notes Server

A small FastAPI practice project for learning basic backend server concepts and a professional development workflow.

This project is not meant to be a full production application. The goal is to learn how a simple Python web server works, how clients send requests, how the server returns JSON responses, and how developers use branches and pull requests to manage work.

---

## Project Goals

By completing this project, you will learn:

- What a backend server is
- What a client is
- What an API is
- What an endpoint is
- How FastAPI routes HTTP requests to Python functions
- How to return JSON responses
- How to use path parameters
- How to use query parameters
- How to receive JSON request bodies
- How to create data using `POST`
- How to save simple data to a JSON file
- How to use `uv` for Python project management
- How to use branches, commits, pull requests, and code review

---

## Tech Stack

This project uses:

- Python
- FastAPI
- Uvicorn
- uv
- JSON file storage
- Git
- GitHub
- GitHub Projects / Kanban board

---

## What You Will Build

By the end of this module, you will build a small Notes API.

The final API will support:

```text
GET  /health
GET  /hello
GET  /notes
GET  /notes?category=web
GET  /notes/{note_id}
POST /notes
```

The app will store notes in a simple `notes.json` file.

---

## Project Structure

The project will eventually look like this:

```text
mini-notes-server/
  README.md
  main.py
  notes.json
  pyproject.toml
  uv.lock
  docs/
    step-0-project-setup.md
    step-1-hello-fastapi-server.md
    step-2-get-notes.md
    step-3-get-note-by-id.md
    step-4-filter-notes.md
    step-5-create-note.md
    step-6-save-notes-to-json.md
```

Some local files or folders may also exist:

```text
.venv/
.python-version
.gitignore
```

The `.venv/` folder should not be committed to GitHub.

---

## Learning Steps

Follow the steps in order.

| Step | Topic | What You Build |
|---|---|---|
| Step 0 | Project setup with `uv` | Initialize the Python project and install dependencies |
| Step 1 | First FastAPI server | Create `/health` and `/hello` endpoints |
| Step 2 | Return all notes | Create `GET /notes` |
| Step 3 | Get one note by ID | Create `GET /notes/{note_id}` |
| Step 4 | Filter notes | Add `GET /notes?category=web` |
| Step 5 | Create a note | Add `POST /notes` |
| Step 6 | Save notes to JSON | Persist notes in `notes.json` |

Detailed instructions:

- [Step 0. Project Setup with uv](docs/step-0-project-setup.md)
- [Step 1. Run Your First FastAPI Server](docs/step-1-hello-fastapi-server.md)
- [Step 2. Return a List of Notes](docs/step-2-get-notes.md)
- [Step 3. Get One Note by ID](docs/step-3-get-note-by-id.md)
- [Step 4. Filter Notes with Query Parameters](docs/step-4-filter-notes.md)
- [Step 5. Create a Note with POST](docs/step-5-create-note.md)
- [Step 6. Save Notes to a JSON File](docs/step-6-save-notes-to-json.md)

---

## Setup

This project uses `uv`.

To check whether `uv` is installed:

```bash
uv --version
```

After cloning the repository, install dependencies with:

```bash
uv sync
```

If dependencies have not been added yet, Step 0 will guide you through:

```bash
uv init
uv add fastapi uvicorn
```

---

## Running the Server

After the FastAPI app has been created, run:

```bash
uv run uvicorn main:app --reload
```

Then open:

```text
http://127.0.0.1:8000
```

FastAPI automatically provides an API documentation page at:

```text
http://127.0.0.1:8000/docs
```

Use `/docs` to test the API endpoints.

---

## Development Workflow

Do not commit directly to `main`.

For each step:

```text
1. Move the task to In Progress on the Kanban board
2. Create a new branch from main
3. Complete the work
4. Test locally
5. Commit the changes
6. Push the branch to GitHub
7. Open a pull request into main
8. Fill out the PR description
9. Review with mentor
10. Merge after approval
11. Move the task to Done
```

Example branch names:

```text
step-0-project-setup
step-1-hello-fastapi-server
step-2-get-notes
step-3-get-note-by-id
step-4-filter-notes
step-5-create-note
step-6-save-notes-to-json
```

---

## Pull Request Template

Each pull request should include:

```markdown
## Summary

What did you add or change?

## Changes

- List the main code or documentation changes

## How I tested it

Include the command you ran and the URLs you tested.

## What I learned

Write 2-3 sentences explaining what you learned.
```

---

## Example PR Description

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

## What I learned

I learned that FastAPI can automatically convert Python lists and dictionaries into JSON responses. I also learned that a backend endpoint can provide data to a client through a URL.
```

---

## Kanban Board Workflow

Use a GitHub Project board with these columns:

```text
Backlog
Ready
In Progress
Review
Done
```

A task should move like this:

```text
Ready → In Progress → Review → Done
```

A task is not considered done until:

```text
- The implementation works
- The code has been pushed
- A pull request has been opened
- The PR has been reviewed
- The PR has been merged
```

---

## Completion Criteria

This module is complete when:

```text
[ ] Steps 0 through 6 are completed
[ ] Each step was done on a separate branch
[ ] Each step has a pull request
[ ] Each PR explains how it was tested
[ ] The final app runs locally
[ ] The final API works in /docs
[ ] Notes persist after restarting the server
[ ] Student can explain the full request/response flow
```

---

## Final Demo

At the end of this module, prepare a short demo.

The demo should show:

- GitHub repository
- Kanban board
- Pull requests
- Running FastAPI server
- FastAPI `/docs` page
- `GET /health`
- `GET /hello`
- `GET /notes`
- `GET /notes/{note_id}`
- `GET /notes?category=web`
- `POST /notes`
- `notes.json`
- Notes still existing after server restart

The student should be able to explain:

```text
A client sends an HTTP request.
FastAPI matches the request to an endpoint.
The Python function runs.
The function reads or creates data.
The server returns JSON.
Data can be stored in memory or persisted in a file.
```

---

## Future Extensions

After this module, possible next steps include:

- Use proper HTTP status codes with `HTTPException`
- Add `DELETE /notes/{note_id}`
- Add `PUT` or `PATCH /notes/{note_id}`
- Move from `notes.json` to SQLite
- Add automated tests
- Build a small frontend that calls this API
- Deploy the API to a cloud server
