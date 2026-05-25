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
uvicorn main:app --reload
```

---

## Project Structure

At the beginning, the project will look like this:

```text
mini-notes-server/
  README.md
  main.py
```

Later, we may add more files such as:

```text
mini-notes-server/
  README.md
  main.py
  notes.json
```

---

# Step 0. Project Setup

## Goal

The goal of Step 0 is to prepare a basic Python project for building a simple FastAPI server.

In this step, we will not build the actual API yet.  
We will only set up the project folder, create a Python virtual environment, install the required packages, and create the first Python file.

---

## 1. Create a Project Folder

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

## 2. Create a Python Virtual Environment

A virtual environment is an isolated Python environment for one project.

This is useful because different Python projects may need different packages or different package versions.

Create a virtual environment:

```bash
python -m venv .venv
```

This creates a folder named `.venv`.

That folder contains the Python environment for this project.

Your folder now looks something like this:

```text
mini-notes-server/
  .venv/
```

---

## 3. Activate the Virtual Environment

Before installing packages, activate the virtual environment.

On Mac or Linux:

```bash
source .venv/bin/activate
```

On Windows:

```bash
.venv\Scripts\activate
```

After activation, your terminal may show something like this:

```text
(.venv) $
```

The `(.venv)` part means the virtual environment is active.

From now on, when you install Python packages, they will be installed inside this project’s virtual environment instead of globally on your computer.

---

## 4. Install FastAPI and Uvicorn

Install the required packages:

```bash
pip install fastapi uvicorn
```

We are installing two packages:

```text
fastapi: the framework for building the API
uvicorn: the program that runs the FastAPI server
```

To check whether they were installed, run:

```bash
pip list
```

You should see `fastapi` and `uvicorn` in the list.

---

## 5. Create `main.py`

Now create a Python file named `main.py`.

On Mac or Linux:

```bash
touch main.py
```

On Windows:

```bash
type nul > main.py
```

You can also create this file manually in VS Code.

Your folder structure should now look like this:

```text
mini-notes-server/
  .venv/
  README.md
  main.py
```

The `main.py` file will contain our FastAPI application code in the next step.

---

## 6. Open the Project in VS Code

If you use VS Code, run this command from inside the project folder:

```bash
code .
```

This opens the current folder in VS Code.

Make sure you can see these files and folders in the VS Code Explorer:

```text
mini-notes-server
README.md
main.py
.venv
```

---

## Step 0 Completion Checklist

You are done with Step 0 if you completed the following:

```text
[ ] Created the mini-notes-server folder
[ ] Moved into the project folder
[ ] Created a Python virtual environment named .venv
[ ] Activated the virtual environment
[ ] Installed fastapi and uvicorn
[ ] Created main.py
[ ] Created README.md
[ ] Opened the project in VS Code
```

---

## Key Ideas to Understand

By the end of Step 0, you should understand these basic ideas:

```text
A server is a program that waits for requests and sends responses.

FastAPI is a Python framework for building web APIs.

Uvicorn is used to run a FastAPI application.

A virtual environment keeps Python packages isolated for one project.

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
