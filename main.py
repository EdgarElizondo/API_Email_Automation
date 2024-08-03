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
    api_info.append((article["title"],article["description"]))

send_email(api_info)
print("Daily News Send!")