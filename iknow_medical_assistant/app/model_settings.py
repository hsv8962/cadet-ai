# Model configuration
import os

DEFAULT_MODEL = os.getenv("LLM_MODEL", "llama3")  # can be overridden via .env
MODEL_SOURCE = os.getenv("MODEL_SOURCE", "ollama")  # e.g., "ollama" or "openai"