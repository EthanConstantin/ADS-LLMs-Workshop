from huggingface_hub import login, HfApi

# Paste API key
api_key = "" #API key goes here

# Log in
login(token=api_key)

# Verify authentication
api = HfApi() 
user_info = api.whoami()

print(f"Authenticated as: {user_info['name']}")
