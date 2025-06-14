# config.py – central configuration for iKnow Medical Assistant
import os
from pathlib import Path

# Base directory
BASE_DIR = Path(__file__).resolve().parent.parent

# Ollama settings
OLLAMA_BASE_URL = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")
OLLAMA_TIMEOUT = 30

# OpenAI fallback
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", None)
OPENAI_MODEL = os.getenv("OPENAI_MODEL", "gpt-3.5-turbo")

# App metadata
APP_NAME = "iKnow Medical Assistant"
VERSION = "0.1.0"

# PDF upload settings
MAX_FILE_SIZE_MB = 200
ALLOWED_EXTENSIONS = [".pdf"]

# Debug
DEBUG = os.getenv("DEBUG", "false").lower() == "true"

