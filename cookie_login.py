# 这个脚本演示了如何使用requests库来处理cookie。
# 使用session对象可以在多个请求之间保持cookie的状态。
import requests

# 创建一个会话对象
session = requests.session()

data = {
    "loginName": "18293153985",
    "password": "Lujia102222"
}

url = "https://www.17k.com/ck/user/login"
session.post(url, data=data)

resp = session.get('https://user.17k.com/ck/author2/shelf?page=1&appKey=2406394919')
print(resp.json())