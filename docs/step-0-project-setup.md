# Step 0. Project Setup with uv

## Goal

The goal of this step is to set up a basic Python project for building a simple FastAPI server.

Before writing any code, we will first understand a few basic backend concepts:

- What is a server?
- What is an API?
- What is FastAPI?
- What is Uvicorn?
- What is uv?

Then we will set up the project using `uv`.

By the end of this step, you should have a Python project ready for Step 1.

---

# 1. What Is a Server?

A server is a program that waits for requests and sends back responses.

For example, when you open a website in a browser, your browser sends a request to a server. The server receives the request, processes it, and sends back a response.

A simplified version looks like this:

```text
Client or Browser  →  Request  →  Server
Client or Browser  ←  Response ←  Server
```

In this project, our server will be a Python program.

Later, when the server is running, we will be able to visit URLs such as:

```text
http://127.0.0.1:8000/hello
http://127.0.0.1:8000/notes
```

When the browser visits one of those URLs, the FastAPI server will receive the request and return a response.

The important idea is:

```text
A server is not just a file.
A server is a running program.
It must be running in order to respond to requests.
```

---

# 2. What Is a Client?

A client is a program that sends requests to a server.

Examples of clients include:

```text
Web browser
Mobile app
Frontend web app
curl
Postman
Another backend service
```

In this project, we will mostly use the browser and FastAPI’s `/docs` page as our clients.

Later, a frontend application could also become a client of this API.

---

# 3. What Is an API?

API stands for Application Programming Interface.

In web development, an API is a way for one program to communicate with another program.

For example:

```text
Frontend app asks: "Give me all notes."
Backend API responds: "Here is a list of notes in JSON."
```

A web API usually exposes endpoints such as:

```text
GET /notes
GET /notes/1
POST /notes
```

Each endpoint represents an action the client can ask the server to perform.

In this project, we will eventually build endpoints such as:

```text
GET /health
GET /hello
GET /notes
GET /notes/{note_id}
GET /notes?category=web
POST /notes
```

---

# 4. What Is an Endpoint?

An endpoint is a specific URL path that the server responds to.

For example:

```text
GET /hello
```

means:

```text
When the client sends a GET request to /hello,
the server should run the code connected to /hello
and return a response.
```

In FastAPI, an endpoint will look like this:

```python
@app.get("/hello")
def hello():
    return {"message": "Hello, FastAPI!"}
```

This means:

```text
When someone sends a GET request to /hello,
run the hello() function,
and return the result as JSON.
```

---

# 5. What Is JSON?

JSON is a common format for sending data between a client and a server.

It looks similar to a Python dictionary, but it is a text format used across many programming languages.

Example JSON response:

```json
{
  "message": "Hello, FastAPI!"
}
```

Example list of notes:

```json
[
  {
    "id": 1,
    "title": "Learn FastAPI",
    "category": "study"
  },
  {
    "id": 2,
    "title": "What is a server?",
    "category": "concept"
  }
]
```

In this project, our FastAPI server will return JSON responses.

---

# 6. What Is FastAPI?

FastAPI is a Python framework for building web APIs.

FastAPI helps us:

- Create API endpoints
- Connect URL paths to Python functions
- Receive data from requests
- Return JSON responses
- Validate input data
- Generate automatic API documentation

Example:

```python
from fastapi import FastAPI

app = FastAPI()


@app.get("/hello")
def hello():
    return {"message": "Hello, FastAPI!"}
```

This creates a small web API with one endpoint:

```text
GET /hello
```

---

# 7. What Is Uvicorn?

FastAPI defines the web application, but we still need a program to actually run it as a server.

That is what Uvicorn does.

You can think of it like this:

```text
FastAPI = the framework for defining the API
Uvicorn = the server program that runs the FastAPI app
```

Later, we will run the server with:

```bash
uv run uvicorn main:app --reload
```

This starts the server locally so your browser can send requests to it.

---

# 8. What Is uv?

`uv` is a modern Python project and package management tool.

In this project, we will use `uv` to:

- Initialize the Python project
- Manage dependencies
- Create and manage the local virtual environment
- Run commands inside the correct project environment

Instead of manually doing this:

```bash
python -m venv .venv
source .venv/bin/activate
pip install fastapi uvicorn
```

we will use:

```bash
uv init
uv add fastapi uvicorn
uv run ...
```

This gives us a cleaner and more professional Python project workflow.

---

# 9. Expected Final Project Structure

After Step 0, the project should look something like this:

```text
mini-notes-server/
  README.md
  main.py
  pyproject.toml
  uv.lock
  docs/
    step-0-project-setup.md
```

You may also see:

```text
.venv/
.python-version
.gitignore
```

That is okay.

Important:

```text
.venv/ should not be committed to GitHub.
```

The `.venv` folder is the local Python environment created by `uv`.

---

# 10. Check Whether uv Is Installed

Open a terminal and run:

```bash
uv --version
```

If you see a version number, `uv` is already installed.

Example:

```text
uv 0.x.x
```

If the command does not work, install `uv`.

---

# 11. Install uv If Needed

## Mac or Linux

Run:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

After installation, close and reopen your terminal if needed.

Then check again:

```bash
uv --version
```

## Windows PowerShell

Run:

```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

After installation, close and reopen your terminal if needed.

Then check again:

```powershell
uv --version
```

---

# 12. Create the Project Folder

Move to the location where you want to create the project.

Then run:

```bash
mkdir mini-notes-server
cd mini-notes-server
```

Confirm that you are inside the project folder.

On Mac or Linux:

```bash
pwd
```

On Windows:

```powershell
cd
```

You should be inside:

```text
mini-notes-server
```

---

# 13. Initialize the Project with uv

Inside the `mini-notes-server` folder, run:

```bash
uv init
```

This initializes the current folder as a Python project.

It may create files such as:

```text
README.md
main.py
pyproject.toml
.python-version
.gitignore
```

The most important file for now is:

```text
pyproject.toml
```

This file describes the Python project and its dependencies.

---

# 14. Add FastAPI and Uvicorn

Run:

```bash
uv add fastapi uvicorn
```

This adds the dependencies needed to build and run the FastAPI server.

After this command, you should see or eventually get these files:

```text
pyproject.toml
uv.lock
```

The `pyproject.toml` file lists the project dependencies.

The `uv.lock` file records the exact dependency versions so the project can be reproduced more reliably.

---

# 15. Confirm the Project Environment Works

Run:

```bash
uv run python --version
```

This runs Python inside the project environment managed by `uv`.

Then run:

```bash
uv run python -c "import fastapi; print(fastapi.__version__)"
```

If FastAPI is installed correctly, this should print a FastAPI version number.

---

# 16. Check the Project Structure

Your project should now look something like this:

```text
mini-notes-server/
  README.md
  main.py
  pyproject.toml
  uv.lock
```

You may also see:

```text
.venv/
.python-version
.gitignore
```

That is okay.

Important note:

```text
.venv/ should not be committed to GitHub.
```

The `.gitignore` file created by `uv init` should normally ignore `.venv/`.

The files that should be committed include:

```text
README.md
main.py
pyproject.toml
uv.lock
docs/
```

---

# 17. Open the Project in VS Code

From inside the project folder, run:

```bash
code .
```

This opens the current folder in VS Code.

In the VS Code Explorer, confirm that you can see files such as:

```text
README.md
main.py
pyproject.toml
uv.lock
```

---

# 18. Optional: Run the Default main.py

Depending on what `uv init` created, `main.py` may contain a simple default program.

You can test it with:

```bash
uv run main.py
```

If it prints a simple message, that means `uv run` is working.

In Step 1, we will replace the contents of `main.py` with FastAPI server code.

---

# 19. Commit the Step 0 Setup

Check the current Git status:

```bash
git status
```

Add the files:

```bash
git add README.md main.py pyproject.toml uv.lock .gitignore .python-version docs/step-0-project-setup.md
```

If some files do not exist, remove them from the command and run it again.

Commit:

```bash
git commit -m "Set up project with uv"
```

Push your branch:

```bash
git push -u origin step-0-project-setup
```

---

# 20. Open a Pull Request

Open a pull request from:

```text
step-0-project-setup
```

into:

```text
main
```

Use this PR title:

```text
Set up project with uv
```

Use this PR description:

```markdown
## Summary

Set up the initial Python project using uv.

## Changes

- Initialized the project with uv
- Added FastAPI and Uvicorn dependencies
- Confirmed the project environment works
- Added Step 0 setup instructions

## How I tested it

I ran:

```bash
uv --version
uv run python --version
uv run python -c "import fastapi; print(fastapi.__version__)"
```

## What I learned

Write 2-3 sentences about what you learned.
```

---

# 21. Step 0 Completion Checklist

You are done with Step 0 if you completed the following:

```text
[ ] Read the sections about server, client, API, endpoint, JSON, FastAPI, Uvicorn, and uv
[ ] Confirmed uv is installed
[ ] Created the mini-notes-server folder
[ ] Initialized the project with uv init
[ ] Added FastAPI and Uvicorn using uv add
[ ] Confirmed pyproject.toml exists
[ ] Confirmed uv.lock exists
[ ] Confirmed FastAPI can be imported
[ ] Opened the project in VS Code
[ ] Confirmed .venv is not meant to be committed
[ ] Committed the setup changes
[ ] Pushed the branch to GitHub
[ ] Opened a pull request
```

---

# 22. Questions to Answer

Before moving to Step 1, make sure you can answer these questions:

```text
1. What is a server?
2. What is a client?
3. What is an API?
4. What is an endpoint?
5. What is JSON?
6. What is FastAPI?
7. What is Uvicorn?
8. What is uv?
9. What does uv init do?
10. What does uv add fastapi uvicorn do?
11. What is pyproject.toml used for?
12. What is uv.lock used for?
13. What does uv run do?
14. Why should .venv not be committed to GitHub?
15. Why do we use a branch and pull request for this step?
```

---

# 23. Key Ideas

The most important ideas from this step are:

```text
A server is a running program that waits for requests and sends responses.

A client sends requests to a server.

An API is a way for programs to communicate.

An endpoint is a specific URL path the server responds to.

JSON is a common data format for API responses.

FastAPI is used to build the API.

Uvicorn is used to run the FastAPI server.

uv manages the Python project environment and dependencies.

pyproject.toml describes the project and its dependencies.

uv.lock records exact dependency versions.

uv run runs commands inside the project environment.

This project will use branches and pull requests for each step.
```

---

# Next Step

In Step 1, we will write the first FastAPI server code.

We will create:

```text
GET /health
GET /hello
```

Then we will run the server locally using:

```bash
uv run uvicorn main:app --reload
```
