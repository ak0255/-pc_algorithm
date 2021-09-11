import requests
from bs4 import BeautifulSoup

print("给我爬！！！")

fa_url = "https://www.pearvideo.com/"
fa_resp = requests.get(fa_url + "category_4")
# print(fa_resp)

fa_page = BeautifulSoup(fa_resp.text, "html.parser")
div_list = fa_page.find_all("div", attrs={"class":"vervideo-bd"})

cnt = 0
for div in div_list :
    a = div.find("a")
    # print(a.get("href"))

    child_href = fa_url + a.get("href")
    # print(child_href)
    
    contId = child_href.split("_")[1]
    child_url = f"https://www.pearvideo.com/videoStatus.jsp?contId={contId}&mrd=0.20029046747735246"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36",
        "Referer": child_href
    }
    child_resp = requests.get(child_url, headers=headers)
    dic = child_resp.json()

    srcUrl = dic["videoInfo"]["videos"]["srcUrl"]
    systemTime = dic["systemTime"]

    srcUrl = srcUrl.replace(systemTime, "cont-" + contId)
    # print(srcUrl)
    with open("E:\VS\Py_Project\数据存储\梨视频娱乐\\" + "第" + str(cnt) + "个视频.mp4", mode="wb") as f :
        f.write(requests.get(srcUrl).content)
    
    cnt += 1
    print("over---" + "第" + str(cnt) + "个视频！！！")
    
    # https://video.pearvideo.com/mp4/third/20210827/cont-1740140-10887340-154020-hd.mp4
    # https://video.pearvideo.com/mp4/third/20210827/1630414742768-10887340-154020-hd.mp4
    
