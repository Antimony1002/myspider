import requests

url = "https://www.pearvideo.com/video_1805319"
contID = url.split("_")[1]

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36",
    "Referer": url
}

videoStatus = f"https://www.pearvideo.com/videoStatus.jsp?contId={contID}&mrd=0.7607544348756171"
resp = requests.get(videoStatus, headers=headers)   # 记得添加headers！
dic = resp.json()   # 括号不要忘了加！

# https://video.pearvideo.com/mp4/short/20260305/cont-1805319-16073264-hd.mp4
# https://video.pearvideo.com/mp4/short/20260305/1773243909126-16073264-hd.mp4
srcUrl = dic['videoInfo']['videos']['srcUrl']
systemTime = dic['systemTime']  # 一定别拼错！！
srcUrl = srcUrl.replace(systemTime, f"cont-{contID}")
with open("b.mp4", mode="wb") as f:
    f.write(requests.get(srcUrl).content)