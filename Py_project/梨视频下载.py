import requests


url = "https://www.pearvideo.com/video_1740397"
contId = url.split("_")[1]
# print(contId)

videoStatusUrl = f"https://www.pearvideo.com/videoStatus.jsp?contId={contId}&mrd=0.8820321169948775"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36",
    "Referer": "https://www.pearvideo.com/video_1740397"
}

resp = requests.get(videoStatusUrl, headers=headers)
dic = resp.json()

srcUrl = dic['videoInfo']['videos']['srcUrl']
systemTime = dic['systemTime']

srcUrl = srcUrl.replace(systemTime, f"cont-{contId}")

# 下载视频
with open("a.mp4", mode="wb") as f :
    f.write(requests.get(srcUrl).content)
