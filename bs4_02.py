import requests
from bs4 import BeautifulSoup

url = "https://wallpapercave.com/magic-wallpapers"
n=1

resp = requests.get(url)
encoding = "utf-8"
page = BeautifulSoup(resp.text, "html.parser")

wallpapers = page.find_all("a", attrs={"class": "wpinkw"})
for wallpaper in wallpapers:
    paper_url = "https://wallpapercave.com" + wallpaper.get("href") + ".jpg"
    img_resp = requests.get(paper_url)
    with open(f"{n}.jpg", mode="wb") as f:
        f.write(img_resp.content)
    n += 1

f.close()