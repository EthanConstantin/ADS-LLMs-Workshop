# ADS-LLMs-Workshop
A Workshop targeted to beginners covering how to make a basic chatbot with the huggingface api 

Install python here: python.org
Install VSCode here: https://code.visualstudio.com/download

How to get your huggingface API key
Make  huggingface account here: https://huggingface.co/

After you create your account, click on your profile in the top right then click Settings
![image](https://github.com/user-attachments/assets/e3669475-e16e-4033-a83c-8c030901b26a)

Then, from the sidebar on the left click on Access Tokens, and then Create new token
![image](https://github.com/user-attachments/assets/40d0a976-e00a-42a7-a432-f061d3ba1301)

Name your token whatever you like, and select the Write option at the top. Then select create token.
![image](https://github.com/user-attachments/assets/21edd701-a297-472d-8cec-46ed073f5d6f)

After you create your api key paste it into the starter files.


## Ideas to enhance the chatbot:
### Easy
- Give the ai a personality (Hint: Give the ai a prompt before starting to the conversation)
- Make Command based responses. (help, about, clear history)
- Show the user that the model is "typing" while it loads

### Intermediate
- Track conversation length. Maybe limiting conversation history improves responses?
- Collect the user's personal information

### Advanced
- Integrate external apis to give the ai specialized knowledge
- Store information between sessions
- Sentiment analysis

## Other example models to load:
- openai-community/gpt2
- mistralai/Mistral-Nemo-Instruct-2407
- HuggingFaceH4/zephyr-7b-beta
