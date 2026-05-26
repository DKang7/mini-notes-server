# Step 0. Project Setup with uv

## Goal

The goal of this step is to set up a basic Python project for building a simple FastAPI server.

In this step, you will:

- Install or confirm `uv`
- Create the project folder
- Initialize a Python project using `uv`
- Add FastAPI and Uvicorn as dependencies
- Confirm that the project environment works
- Open the project in VS Code

We will not build the actual API yet. That starts in Step 1.

---

## What Is uv?

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

## What Is FastAPI?

FastAPI is a Python framework for building web APIs.

A web API lets one program communicate with another program over HTTP.

For example:

```text
Client asks:  GET /notes
Server sends: JSON list of notes
```

Later in this project, we will create API endpoints such as:

```text
GET /health
GET /hello
GET /notes
POST /notes
```

---

## What Is Uvicorn?

FastAPI defines the web application, but we need something to actually run it as a server.

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

---

# 1. Check Whether uv Is Installed

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

# 2. Install uv If Needed

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

# 3. Create the Project Folder

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

# 4. Initialize the Project with uv

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

# 5. Add FastAPI and Uvicorn

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

# 6. Confirm the Project Environment Works

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

# 7. Check the Project Structure

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

# 8. Open the Project in VS Code

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

# 9. Optional: Run the Default main.py

Depending on what `uv init` created, `main.py` may contain a simple default program.

You can test it with:

```bash
uv run main.py
```

If it prints a simple message, that means `uv run` is working.

In Step 1, we will replace the contents of `main.py` with FastAPI server code.

---

# 10. Commit the Step 0 Setup

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

# 11. Open a Pull Request

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

# 12. Step 0 Completion Checklist

You are done with Step 0 if you completed the following:

```text
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

# 13. Questions to Answer

Before moving to Step 1, make sure you can answer these questions:

```text
1. What is uv?
2. What does uv init do?
3. What does uv add fastapi uvicorn do?
4. What is pyproject.toml used for?
5. What is uv.lock used for?
6. What does uv run do?
7. What is FastAPI?
8. What is Uvicorn?
9. Why should .venv not be committed to GitHub?
10. Why do we use a branch and pull request for this step?
```

---

# 14. Key Ideas

The most important ideas from this step are:

```text
uv manages the Python project environment and dependencies.

pyproject.toml describes the project and its dependencies.

uv.lock records exact dependency versions.

uv run runs commands inside the project environment.

FastAPI is used to build the API.

Uvicorn is used to run the FastAPI server.

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
