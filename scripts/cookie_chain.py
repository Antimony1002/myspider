import requests

# 拉取视频的网址
url = "https://www.pearvideo.com/video_1805300"
contId = url.split("_")[1]

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36",
    # 防盗链溯源
    "Referer": url
}

videoStatus = f"https://www.pearvideo.com/videoStatus.jsp?contId={contId}&mrd=0.34517971567648564"
resp = requests.get(videoStatus, headers=headers)
dic = resp.json()
srcUrl = dic['videoInfo']['videos']['srcUrl']
systemTime = dic['systemTime']

# https://video.pearvideo.com/mp4/short/20260304/cont-1805300-16073177-hd.mp4
# https://video.pearvideo.com/mp4/short/20260304/1773241686512-16073177-hd.mp4
# 替换srcUrl

srcUrl = srcUrl.replace(systemTime, f"cont-{contId}")
with open("a.mp4", mode="wb") as f:
    f.write(requests.get(srcUrl).content)