import os
from dotenv import load_dotenv
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

env_file = BASE_DIR / ".env"

load_dotenv(env_file)

class Settings:

    OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

    OPENROUTER_BASE_URL = os.getenv(
        "OPENROUTER_BASE_URL",
        "https://openrouter.ai/api/v1"
    )

    MODEL_NAME = os.getenv(
        "OPENROUTER_MODEL",
        os.getenv("MODEL_NAME", "inclusionai/ring-2.6-1t:free")
    )

settings = Settings()