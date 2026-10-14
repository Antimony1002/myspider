import requests
from bs4 import BeautifulSoup

f = open("wallpaper_fantasy.csv", mode="w", encoding="utf-8")
base_url = "https://wallpapercave.com/categories/fantasy"

base_resp = requests.get(base_url)
encoding = "utf-8"
base_page = BeautifulSoup(base_resp.text, "html.parser")

catagories = base_page.find_all("div", attrs={"class": "albumphoto"})
for catagory in catagories:
    url = "https://wallpapercave.com" + catagory.get("href")
    resp = requests.get(url)
    encoding = "utf-8"
    page = BeautifulSoup(resp.text, "html.parser")

    wallpapers = page.find_all("a", attrs={"class": "wpinkw"})
    for wallpaper in wallpapers:
        paper_url = "https://wallpapercave.com" + wallpaper.get("href") + ".jpg"
        f.write(paper_url + "\n")
f.close()