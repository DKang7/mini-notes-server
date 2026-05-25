# Mini Notes Server

A small FastAPI practice project for learning basic backend server concepts.

This project is not intended to be a full application yet.  
The main goal is to understand how a simple Python web server works, how a client sends requests, and how the server returns responses.

---

## Learning Goals

By working through this project, you will learn:

- What a server is
- What an API is
- How FastAPI works
- How to create and run a simple Python web server
- How a browser or client sends requests to a server
- How the server returns JSON responses
- How to manage a Python project using `uv`
- How to organize a small backend project

---

## What Is a Server?

A server is a program that waits for requests and sends back responses.

For example, when you open a website in a browser, the browser sends a request to a server. The server receives the request, processes it, and sends back a response.

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

---

## What Is an API?

API stands for Application Programming Interface.

In web development, an API is a way for one program to communicate with another program.

For example:

```text
Frontend app asks: "Give me all notes."
Backend API responds: "Here is a list of notes in JSON."
```

In this project, we will build API endpoints such as:

```text
GET /health
GET /hello
GET /notes
POST /notes
```

Each endpoint will be connected to a Python function.

---

## What Is FastAPI?

FastAPI is a Python framework for building web APIs.

FastAPI lets us define routes using Python decorators.

For example:

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

FastAPI is useful because it makes it easy to:

- Create API endpoints
- Receive data from requests
- Return JSON responses
- Validate input data
- Generate automatic API documentation

---

## What Is Uvicorn?

FastAPI defines the web application, but we still need a program to actually run it.

That is what Uvicorn does.

You can think of it like this:

```text
FastAPI = the web app framework
Uvicorn = the server runner that starts the FastAPI app
```

Later, we will run the server with:

```bash
uv run uvicorn main:app --reload
```

---

## What Is uv?

`uv` is a modern Python project and package management tool.

In this project, we will use `uv` to:

- Create the Python project structure
- Manage dependencies
- Create and manage the virtual environment automatically
- Run Python commands inside the project environment

Instead of manually running:

```bash
python -m venv .venv
pip install fastapi uvicorn
```

we will use:

```bash
uv init
uv add fastapi uvicorn
```

Then, when we run the server, we will use:

```bash
uv run uvicorn main:app --reload
```

This makes the project setup more consistent and closer to a modern Python development workflow.

---

## Project Structure

After Step 0, the project will look like this:

```text
mini-notes-server/
  README.md
  main.py
  pyproject.toml
  uv.lock
```

You may also see:

```text
mini-notes-server/
  .venv/
```

The `.venv` folder is the local virtual environment created by `uv`.  
It should not be committed to GitHub.

Later, we may add more files such as:

```text
mini-notes-server/
  README.md
  main.py
  pyproject.toml
  uv.lock
  docs/
    step-1-hello-fastapi-server.md
  notes.json
```

---

# Step 0. Project Setup with uv

## Goal

The goal of Step 0 is to prepare a basic Python project for building a simple FastAPI server.

In this step, we will not build the actual API yet.  
We will set up the project folder, initialize the Python project with `uv`, install the required packages, and create the first Python file.

---

## 1. Install uv

First, make sure `uv` is installed.

Check whether `uv` is available:

```bash
uv --version
```

If you see a version number, `uv` is already installed.

If not, install `uv`.

On Mac or Linux:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

On Windows PowerShell:

```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

After installing, close and reopen the terminal if needed.

Then check again:

```bash
uv --version
```

---

## 2. Create a Project Folder

Open a terminal and move to the location where you want to create the project.

Then run:

```bash
mkdir mini-notes-server
cd mini-notes-server
```

This creates a new folder called `mini-notes-server` and moves into it.

Check your current location:

```bash
pwd
```

On Windows, you can use:

```bash
cd
```

At this point, you should be inside the `mini-notes-server` folder.

---

## 3. Initialize the Project with uv

Run:

```bash
uv init
```

This initializes the folder as a Python project.

It may create files such as:

```text
pyproject.toml
README.md
main.py
```

The most important file is:

```text
pyproject.toml
```

This file stores project information and dependencies.

If `uv init` creates a default `main.py`, you can keep it for now. We will replace its contents in Step 1.

---

## 4. Add FastAPI and Uvicorn

Add the packages needed for this project:

```bash
uv add fastapi uvicorn
```

This does several things:

```text
Adds fastapi and uvicorn as project dependencies
Updates pyproject.toml
Creates or updates uv.lock
Creates a local virtual environment if needed
```

After this step, your project should include:

```text
pyproject.toml
uv.lock
```

The `uv.lock` file stores the exact resolved package versions.  
This helps other developers install the same dependency versions.

---

## 5. Confirm the Project Environment

Run:

```bash
uv run python --version
```

This runs Python inside the project environment managed by `uv`.

Then run:

```bash
uv run python -c "import fastapi; print(fastapi.__version__)"
```

If this prints a FastAPI version number, FastAPI is installed correctly.

---

## 6. Check the Project Structure

Your folder should now look something like this:

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
```

That is the local virtual environment. It should stay on your computer and should not be committed to GitHub.

---

## 7. Open the Project in VS Code

If you use VS Code, run this command from inside the project folder:

```bash
code .
```

This opens the current folder in VS Code.

Make sure you can see these files in the VS Code Explorer:

```text
README.md
main.py
pyproject.toml
uv.lock
```

---

## 8. Step 0 Completion Checklist

You are done with Step 0 if you completed the following:

```text
[ ] Installed uv
[ ] Created the mini-notes-server folder
[ ] Moved into the project folder
[ ] Ran uv init
[ ] Added fastapi and uvicorn using uv add
[ ] Confirmed that pyproject.toml exists
[ ] Confirmed that uv.lock exists
[ ] Confirmed that FastAPI can be imported
[ ] Opened the project in VS Code
```

---

## 9. Key Ideas to Understand

By the end of Step 0, you should understand these basic ideas:

```text
A server is a program that waits for requests and sends responses.

FastAPI is a Python framework for building web APIs.

Uvicorn is used to run a FastAPI application.

uv manages the Python project, dependencies, and virtual environment.

pyproject.toml describes the Python project and its dependencies.

uv.lock records the exact dependency versions.

main.py will be the main file where we write our server code.

README.md explains what the project is and how to set it up.
```

The most important idea is this:

```text
We are preparing a Python program that will eventually run continuously as a server.

When a browser or client sends a request to it,
our Python code will decide what response to send back.
```

---

## Next Step

In Step 1, we will write the first FastAPI code and run the server locally.

We will create simple endpoints such as:

```text
GET /health
GET /hello
```

Then we will test them in the browser.
