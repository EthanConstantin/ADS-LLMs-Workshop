# Step 1: Set up the connection to the model
import requests

MODEL = "mistralai/Mistral-Nemo-Instruct-2407"  # Name of the model we will be using
API_URL = f"https://api-inference.huggingface.co/models/{MODEL}"
HEADERS = {"Authorization": "Bearer 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"}  # Replace my Api Key with yours

"""Function to get a response from the api"""
def query(payload):
    response = requests.post(API_URL, headers=HEADERS, json=payload)
    return response.json()

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Step 2: Make a conversation loop

# Initialize conversation history
conversation_history = ""

while True:
    user_input = input("You: ")  # Take input from the user (you) from the console

    if user_input.lower() == "exit":  # If the input is 'exit' exit the loop and stop the conversation
        print("Chatbot: Goodbye!")
        break

    # Append user input to conversation history
    conversation_history += f"User: {user_input}\n"

    # Create the request payload
    payload = {
        "inputs": conversation_history,
        "parameters": {
            "max_length": 200,  # Optional: Adjust response length
            "temperature": 0.7,  # Optional: Control randomness of the response. Lower values make the response more deterministic
        }
    }

    # Send the input to the API
    response = query(payload)

    # Extract the generated text from the API response
    # if isinstance(response, dict) and 'generated_text' in response:
    #     chatbot_reply = response['generated_text']
    # else:
    #     chatbot_reply = "I couldn't generate a response."
    chatbot_reply = response[0]['generated_text']

    # Display the chatbot's reply
    print("Chatbot:", chatbot_reply)

    # Append chatbot response to conversation history
    conversation_history += f"Chatbot: {chatbot_reply}\n"





# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Step 4: Enhancing the chatbot

# Easy
# - Give the ai a personality (Hint: Give the ai a prompt before starting to the conversation)
# - Make Command based responses. (help, about, clear history)
# - Show the user that the model is "typing" while it loads

# Intermediate
# - Track conversation length. Maybe limiting conversation history improves responses?
# - Collect the user's personal information

# Advanced
# - Integrate external apis to give the ai specialized knowledge
# - Store information between sessions
# - Sentiment analysis