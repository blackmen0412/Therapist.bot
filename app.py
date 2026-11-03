from fastapi import FastAPI
from pydantic import BaseModel
from transformers import pipeline
from transformers.utils import logging
import torch

logging.set_verbosity_error()

app = FastAPI()

MODEL_PATH = "./gemma-therapist-full"

print("Loading Therapist Model...")

pipe = pipeline(
    "text-generation",
    model=MODEL_PATH,
    tokenizer=MODEL_PATH,
    device="mps" if torch.backends.mps.is_available() else -1,
)

print("✅ Model Loaded!")

# Stores conversation for each session
conversations = {}


class ChatRequest(BaseModel):
    session_id: str
    message: str


@app.get("/")
def home():
    return {"message": "Therapist API Running"}


@app.post("/chat")
def chat(req: ChatRequest):

    # Create conversation if new session
    if req.session_id not in conversations:
        conversations[req.session_id] = []

    conversation = conversations[req.session_id]

    conversation.append(
        {
            "role": "user",
            "content": req.message,
        }
    )

    outputs = pipe(
        conversation,
        max_new_tokens=180,
        temperature=0.8,
        top_p=0.9,
        do_sample=True,
    )

    response = outputs[0]["generated_text"][-1]["content"]

    conversation.append(
        {
            "role": "assistant",
            "content": response,
        }
    )

    # Keep last 10 exchanges
    if len(conversation) > 20:
        conversation[:] = conversation[-20:]

    return {
        "response": response
    }