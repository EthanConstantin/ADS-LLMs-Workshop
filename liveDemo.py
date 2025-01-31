import requests

MODEL = "mistralai/Mistral-Nemo-Instruct-2407"  # Name of the model we will be using
API_URL = f"https://api-inference.huggingface.co/models/{MODEL}"
HEADERS = {"Authorization": "Bearer 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"}  # Replace my Api Key with yours

"""Function to get a response from the api"""
def query(payload):
    response = requests.post(API_URL, headers=HEADERS, json=payload)
    return response.json()

# This is the text you will feed into the LLM
input_text = "What is the capital of canada?"

# The ai's response
response = query({"inputs": input_text})
chatbot_reply = response[0]["generated_text"]

print("Chatbot:", chatbot_reply)