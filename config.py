import os
from dotenv import load_dotenv

# Load environment variables from a .env file if it exists
load_dotenv()

# INSTRUCTIONS:
# Get your API key from Google AI Studio (https://aistudio.google.com/)
# You can hardcode it below for testing, but better to use an environment variable.
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY", "YOUR_GEMINI_API_KEY_HERE")

if GOOGLE_API_KEY == "YOUR_GEMINI_API_KEY_HERE":
    print("⚠️ WARNING: Please set your GOOGLE_API_KEY in config.py or your environment variables.")
