from typing import Any

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Email Summarizer API")

# UI integrate karte waqt zaroori hoga
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # production mein apne UI ka URL do
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/summarize")
async def summarize(payload: Any):
    # Abhi sirf JSON receive ho raha hai, processing baad mein
    print(payload)  # debugging ke liye
    return "JSON receive ho gaya"