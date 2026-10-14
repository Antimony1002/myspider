import requests
from bs4 import BeautifulSoup

f = open("weather.csv", mode="w", encoding="utf-8")
url = "https://www.aqi.in/weather/cn/live-ranking"

headers = {
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36"
}

encoding = "utf-8"
resp = requests.get(url, headers=headers)

page = BeautifulSoup(resp.text, "html.parser")
cities = page.find_all('a', class_='location')

for city in cities:
    f.write(city.text + "\n")

f.close()
