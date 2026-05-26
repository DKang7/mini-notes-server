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
    }
]

@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/hello")
def hello():
    return {"message": "My first FastAPI is running!"}

@app.get("/notes")
def get_notes():
    return notes