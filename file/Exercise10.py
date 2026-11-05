import requests
import json
query = input("what type of news are you interested in ? ")
url = f"https://newsapi.org/v2/everything?q={query}&from=2026-11-04&to=2026-11-04&sortBy=popularity&apiKey=c0626b2046054449b8bb783a90dc27c3"
r = requests.get(url)
news = json.loads(r.text)
# print(news, type(news))
for article in news["articles"]:
    print(article["title"])
    print(article["description"])
    print("---------------------------------------------")
