import requests

API_KEY = "7bbd3cf31a41413aa38ef3475630cd2d"
url = "https://newsapi.org/v2/everything?q=tesla&from=2024-07" \
    f"-03&sortBy=publishedAt&apiKey={API_KEY}"

# Get API URL
req = requests.get(url)

# Get Dictionary
content = req.json()

# Accesss data title
for article in content["articles"]:
    print(article["title"])