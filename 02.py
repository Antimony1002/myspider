import requests

url = "https://fanyi.baidu.com/sug"

data = {
    "kw": input("请输入要翻译的内容：")
}

resp = requests.post(url, data=data)
print(resp.json())