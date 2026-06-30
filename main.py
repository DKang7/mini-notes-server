import json
from pathlib import Path

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

NOTES_FILE = Path("notes.json")

class NoteCreate(BaseModel):
    title: str
    content: str
    category: str

def load_notes():
    with open(NOTES_FILE, "r") as file:
        return json.load(file)
    
def save_notes():
    with open(NOTES_FILE, "w") as file:
        json.dump(notes, file, indent=2)


notes = load_notes()
# notes = [
#     {
#         "id": 1,
#         "title": "Learn FastAPI",
#         "content": "FastAPI is a Python framework for building APIs.",
#         "category": "study",
#     },
#     {
#         "id": 2,
#         "title": "What is a server?",
#         "content": "A server is a program that waits for requests and sends responses.",
#         "category": "concept",
#     },
#     {
#         "id": 3,
#         "title": "HTTP GET",
#         "content": "GET is used when the client wants to read data from the server.",
#         "category": "web",
#     },
#     {
#         "id": 4,
#         "title": "API Response",
#         "content": "An API response is the data sent back from the server to the client.",
#         "category": "web",
#     }
# ]

@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/hello")
def hello():
    return {"message": "My first FastAPI is running!"}



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
    save_notes()

    return new_note

@app.get("/notes/{note_id}")
def get_note(note_id: int):
    for note in notes:
        if note["id"] == note_id:
            return note

    return {"error": "Note not found"}
