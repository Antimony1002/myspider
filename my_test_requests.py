# 爬取百度的页面源代码
import requests

url = "http://www.baidu.com"
resp = requests.get(url)
resp.encoding = "utf-8" #设置编码格式
print(resp.text) #拿到页面的源代码