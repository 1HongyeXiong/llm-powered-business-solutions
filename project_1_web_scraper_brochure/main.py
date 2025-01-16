import os
from dotenv import load_dotenv
from stream import stream_brochure

# Initialize and constants
load_dotenv(override=True)
api_key = os.getenv('OPENAI_API_KEY')

if api_key and api_key.startswith('sk-proj-') and len(api_key) > 10:
    print("API key looks good so far")
else:
    print("There might be a problem with your API key? Please visit the troubleshooting notebook!")

stream_brochure("HuggingFace", "https://huggingface.co")
