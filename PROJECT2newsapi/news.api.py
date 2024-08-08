import requests
import json
query=input("What type of news are you interested in?")
url=f"https://newsapi.org/v2/everything?q={query}&from=2023-10-06&sortBy=publishedAt&apiKey=API_KEY"
r=requests.get(url)
print(r.text)
news = json.loads(r.text)
#print(news,type(news))
for article in news["articles"]:
    print(article["title"])
    print(article["description"])
    print("-------------------------------------------")

