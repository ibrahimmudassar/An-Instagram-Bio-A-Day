import requests
from environs import Env  # For environment variables
from instagrapi import Client

# Setting up environment variables
env = Env()
env.read_env()  # read .env file, if it exists

# max length is adjustable to your desire
# https://github.com/lukePeavey/quotable for documentation
response = requests.get(
    "https://api.quotable.io/random?maxLength=80?tags=famous-quotes").json()
full_quote = response['content'] + " - " + response['author']

# sign in to instagram
cl = Client()
cl.login(env("INSTA_USERNAME"), env("INSTA_PASSWORD"))

print(cl.account_info().dict())
cl.account_edit(biography=full_quote)
print(cl.account_info().dict())
