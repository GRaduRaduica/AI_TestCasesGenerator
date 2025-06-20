"""
List of all the available alternative interfaces to use
"""
from huggingface_hub import InferenceClient
from dotenv import load_dotenv
import os
from pathlib import Path


# Get the path of the current script
current_file = Path(__file__).resolve()
# Construct the path to the .env file relative to this script
dotenv_path = current_file.parent.parent / "api_keys" / "protection_huggingface.env"

# Load the .env file
load_dotenv(dotenv_path=dotenv_path)
api_key = os.getenv("API_KEY")


list_of_interfaces = [
    InferenceClient(api_key=api_key),
    InferenceClient(model="tiiuae/falcon-7b-instruct", api_key=api_key),
    InferenceClient(model="mistralai/Mistral-7B-Instruct-v0.2", api_key=api_key),
    InferenceClient(model="openchat/openchat-3.5", api_key=api_key),
    InferenceClient(model="meta-llama/Llama-3.3-70B-Instruct", api_key=api_key),
    InferenceClient(model="microsoft/Phi-3.5-mini-instruct", api_key=api_key),
    InferenceClient(model="mistralai/Mistral-7B-Instruct-v0.3", api_key=api_key),
    InferenceClient(model="mistralai/Mistral-7B-Instruct-v0.4", api_key=api_key)
]


if __name__ == '__main__':
    # print(api_key)
    pass