import requests
import re

f = open("2025bikan.csv", mode="w", encoding='utf-8')
headers = {
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36"
}

url = "https://www.dytt8899.com/"
resp = requests.get(url, headers=headers)
resp.encoding = "gbk"
PageSource = resp.text

obj1 = re.compile(r"2026必看热片.*?<ul>(?P<html>.*?)</ul>", re.S)
result1 = obj1.search(PageSource)
html = result1.group("html")

obj2 = re.compile(r"<li><a href='(?P<href>.*?)' title=(?P<title>.*?)>", re.S)
result2 = obj2.finditer(html)

obj3 = re.compile(r'<div id="Zoom">.*?◎片　　名　(?P<movie_name>.*?)'
                  r'<br />.*?<td style="WORD-WRAP: break-word" bgcolor="#fdfddf"><a href="(?P<download_link>.*?)">', re.S)

for item in result2:
    sub_href = url.strip("/") + item.group("href")
    title = item.group("title")
    sub_resp = requests.get(sub_href, headers=headers)
    sub_resp.encoding = "gbk"
    sub_PageSource = sub_resp.text

    result3 = obj3.search(sub_PageSource)
    movie_name = result3.group('movie_name')
    download_link = result3.group('download_link')
    f.write(f"{movie_name},{download_link}\n")

resp.close()
f.close()
