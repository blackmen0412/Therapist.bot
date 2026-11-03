import torch
from transformers import pipeline
from transformers.utils import logging

logging.set_verbosity_error()

MODEL_PATH = "./gemma-therapist-full"

print("Loading model...")

pipe = pipeline(
    "text-generation",
    model=MODEL_PATH,
    tokenizer=MODEL_PATH,
    device="mps" if torch.backends.mps.is_available() else -1,
)

conversation = []

print("✅ Therapist chatbot is ready!")
print("Type 'exit' to quit.\n")

while True:
    user = input("You: ")

    if user.lower() in ["exit", "quit"]:
        break

    conversation.append(
        {
            "role": "user",
            "content": user,
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

    print(f"\nTherapist: {response}\n")

    conversation.append(
        {
            "role": "assistant",
            "content": response,
        }
    )

    # Keep only last 10 exchanges
    if len(conversation) > 20:
        conversation = conversation[-20:]