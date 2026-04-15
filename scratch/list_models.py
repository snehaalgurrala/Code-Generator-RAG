import os
from google import genai
from dotenv import load_dotenv

load_dotenv()

def test_models():
    try:
        client = genai.Client()
        for m in client.models.list():
            if 'embedContent' in getattr(m, 'supported_generation_methods', []):
                print(f"Supported method embedContent: {m.name}")
            else:
                print(m.name)
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    test_models()
