import requests
import re
'''爬取m3u8
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36"
}

url = "https://91kanju.com/vod-play/54812-1-1.html"
resp = requests.get(url, headers=headers)

obj = re.compile(r"url: '(?P<url>.*?)',", re.S)

m3u8_url = obj.search(resp.text).group("url")
resp.close()

# print(m3u8_url)

resp2 = requests.get(m3u8_url, headers=headers)

with open("哲仁王后.m3u8", mode="wb") as f :
    f.write(resp2.content)
resp2.close()

'''
cnt = 1
with open("E:\VS\Py_Project\数据存储\哲仁王后.m3u8", mode="r", encoding="utf-8") as f :
    for line in f :
        line = line.strip()
        if line.startswith("#") : 
            continue
        resp3 = requests.get(line)
        f = open(f"E:\VS\Py_Project\数据存储\哲仁王后小片段\{cnt}.ts", mode="wb")
        f.write(resp3.content)
        f.close()
        resp3.close()
        cnt += 1
        print("完成了%d个"%cnt)
        # print(line)