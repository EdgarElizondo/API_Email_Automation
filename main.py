import os
import requests
from send_email import send_email

TOPIC = "tesla"
LIMIT_EMAILS = 20
API_KEY = os.getenv("PASSWORD_APINEWS")
url = "https://newsapi.org/v2/everything?" \
    f"q={TOPIC}" \
    "&from=2024-07-03" \
    "&sortBy=publishedAt" \
    f"&apiKey={API_KEY}" \
    "&language=en"

# Get API URL
req = requests.get(url)

# Get Dictionary
content = req.json()

# Message Format
subject = "Daily News"
text = ""
for article in content["articles"][:LIMIT_EMAILS]:
    if article["title"] is not None:
        text += f"Title: {article['title']}\n" \
        + f"Description: {article['description']}\n" \
        + f"Link: {article['url']}\n" \
        + "_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _\n\n"

# Message to be sent
message = f"Subject: {subject}\n\n{text}"

# Send Email
send_email(message.encode("UTF-8"))
print("Daily News Send!")