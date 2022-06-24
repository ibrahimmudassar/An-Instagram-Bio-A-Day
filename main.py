import requests
from environs import Env  # For environment variables
from instagrapi import Client

# Setting up environment variables
env = Env()
env.read_env()  # read .env file, if it exists

footer = "\nMy biography changes everyday!"

# max length is adjustable to your desire
# https://github.com/lukePeavey/quotable for documentation
quote_length = 151  # i need to make sure the bio is 150 or less so i subtract the footer length and then make sure the quote + author is less than that amount
while quote_length > 151 - len(footer):
    response = requests.get(
        "https://api.quotable.io/random?maxLength=80?tags=famous-quotes").json()
    full_quote = response['content'] + " - " + response['author']
    quote_length = len(full_quote)

# sign in to instagram
cl = Client()
cl.login(env("INSTA_USERNAME"), env("INSTA_PASSWORD"))

full_text = full_quote + footer

print(cl.account_info().dict())
cl.account_edit(biography=full_text, external_url="https://t.ly/agks")
print(cl.account_info().dict())
print(len(footer))
print(len(full_text))
