import requests
from send_email import send_email

API_KEY = "7bbd3cf31a41413aa38ef3475630cd2d"
url = "https://newsapi.org/v2/everything?q=tesla&from=2024-07" \
    f"-03&sortBy=publishedAt&apiKey={API_KEY}"

# Get API URL
req = requests.get(url)

# Get Dictionary
content = req.json()

# Get API information
api_info = []
for article in content["articles"]:
    if article["title"] is not None:
        api_info.append((article["title"],article["description"]))

# Message Format
subject = "Daily News"
text = ""
for title, description in api_info:
    text += f"Title: {title}\n" \
        + f"Description:{description}\n\n" \
        + "_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _\n\n"
# Message to be sent
message = 'Subject: {}\n\n{}'.format(subject, text)

# Send Email
send_email(message.encode("UTF-8"))
print("Daily News Send!")