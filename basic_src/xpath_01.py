from lxml import etree
import requests

url = "https://movie.douban.com/top250"
resp = requests.get(url)
resp.encoding = "utf-8"
html = etree.HTML(resp.text)

