import requests

MODEL = "mistralai/Mixtral-8x7B-Instruct-v0.1"  # Name of the model we will be using
API_URL = f"https://api-inference.huggingface.co/models/{MODEL}"
HEADERS = {"Authorization": "Bearer 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"}  # Replace my Api Key with yours

"""Function to get a response from the api"""
def query(payload):
    response = requests.post(API_URL, headers=HEADERS, json=payload)
    return response.json()

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Step 3: Add Conversation history and model parameters

# Initialize conversation history
conversation_history = ""

while True:
    user_input = input("User: ")  # Take input from the user (you) from the console

    if user_input.lower() == "exit":  # If the input is 'exit' exit the loop and stop the conversation
        print("Chatbot: Goodbye!")
        break

    # Append user input to conversation history
    conversation_history += f"User: {user_input}\nChatbot: "

    # Create the request payload
    payload = {
        "inputs": conversation_history,
        "parameters": {
            "temperature": 0.6,  # Optional: Control randomness of the response. Lower values make the response more deterministic (less likely to go off-topic)
            "do_sample": False  # Optional: If set to false the model will always generate the most likely word (deterministic)
        }
    }

    # Send the input to the API
    response = query(payload)

    # Extract the generated text from the API response. Also remove the user's input from the output
    chatbot_reply = response[0]['generated_text'].replace(conversation_history, "").strip()


    # Display the chatbot's reply
    print(chatbot_reply)

    # Append chatbot response to conversation history
    conversation_history += f"{chatbot_reply}\n"


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
# - Integrate external apis to give the ai specialized knowledge (Weather data for example)
# - Store information between sessions
# - Sentiment analysis