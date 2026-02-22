from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from groq import Groq
import os

app = FastAPI()

# Esto permite que tu CodePen se comunique con el servidor
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

client = Groq(api_key="TU_API_KEY_DE_GROQ")

class ChatRequest(BaseModel):
    mensaje: str

@app.get("/")
def home():
    return {"status": "IA funcionando"}

@app.post("/chat")
async def chat(request: ChatRequest):
    completion = client.chat.completions.create(
        messages=[{"role": "user", "content": request.mensaje}],
        model="llama-3.1-8b-instant",
    )
    return {"respuesta": completion.choices[0].message.content}