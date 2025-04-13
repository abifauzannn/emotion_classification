from fastapi import FastAPI, Form
from pydantic import BaseModel

# Definisikan model untuk input request
class TextRequest(BaseModel):
    text: str

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, ABINGGGG!"}

@app.get("/hello/{name}")
def say_hello(name: str):
    return {"message": f"Hello, {name}!"}

@app.post("/casefold")
def casefold_text(text: str = Form(...)):
    casefolded_text = text.casefold()
    return {"original_text": text, "casefolded_text": casefolded_text}