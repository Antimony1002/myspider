import requests
import re
import time

f = open("top250.csv", mode="w", encoding='utf-8')
f.write("电影标题,评分,评价人数\n")

headers = {
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36"
}

# print(resp.text)
obj = re.compile(r'<span class="title">(?P<title>.*?)'
                 r'</span>.*?<span class="rating_num" property="v:average">(?P<score>.*?)'
                 r'</span>.*?<span property="v:best" content="10.0"></span>.*?<span>(?P<num>.*?)人评价</span>', re.S)

for i in range(10):
    start = i*25
    url = f"https://movie.douban.com/top250?start={start}"
    resp = requests.get(url, headers=headers)
    PageSource = resp.text
    result = obj.finditer(PageSource)
    for item in result:
        title = item.group("title")
        score = item.group("score")
        num = item.group("num")
        print(title, score, num)
        f.write(f"{title},{score},{num}\n")
    time.sleep(2)
    resp.close()

f.close()
