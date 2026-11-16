
import os

OLLAMA_URL = os.getenv(
    "OLLAMA_URL",
    "http://localhost:11434"
)

MODEL = os.getenv(
    "MODEL",
    "qwen2.5:3b"
)

API_KEY = os.getenv("API_KEY", "")
