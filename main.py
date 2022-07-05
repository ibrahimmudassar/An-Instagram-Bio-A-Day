import requests
from environs import Env  # For environment variables
from instagrapi import Client
import datetime

# Setting up environment variables
env = Env()
env.read_env()  # read .env file, if it exists

# footer = "\nMy biography changes everyday!"

# # max length is adjustable to your desire
# # https://github.com/lukePeavey/quotable for documentation
# quote_length = 151  # i need to make sure the bio is 150 or less so i subtract the footer length and then make sure the quote + author is less than that amount
# while quote_length > 151 - len(footer):
#     response = requests.get(
#         "https://api.quotable.io/random?maxLength=80?tags=famous-quotes").json()
#     full_quote = response['content'] + " - " + response['author']
#     quote_length = len(full_quote)

# full_text = full_quote + footer


today = datetime.date.today()
future = datetime.date(2022, 11, 8)
diff = future - today
print(diff.days)

# sign in to instagram
cl = Client()
cl.login(env("INSTA_USERNAME"), env("INSTA_PASSWORD"))

if diff.days == 1:
    bio = f"We are 1 day away from Election Day 2022! Click the link below if you plan to vote!"
else:
    bio = f"We are {diff.days} days away from Election Day 2022! Click the link below if you plan to vote!"

cl.account_edit(biography=bio, external_url="https://t.ly/LWj-")
print(cl.account_info().dict())
