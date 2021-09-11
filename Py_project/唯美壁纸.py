import requests
from bs4 import BeautifulSoup
import time

url = "http://www.bizhi360.com/weimei/index.html"
urls = "http://www.bizhi360.com"
resp = requests.get(url)
resp.encoding = "utf-8"
# print(resp.text)

main_page = BeautifulSoup(resp.text, "html.parser")
a_lists = main_page.find("div", attrs={"class":"pic-list"}).find_all("a")[1:9]
a_lists.pop(3)
# print(a_lists)

cnt = 1
for a_list in a_lists :
    # print(a_list.get("href"))
    child_url = urls + a_list.get("href")# 通过get方法拿到href属性的值，再拼接成子页面url
    child_resp = requests.get(child_url)# 访问子页面
    child_resp.encoding = "utf-8"
    # print(child_resp.text)
    child_page = BeautifulSoup(child_resp.text, "html.parser")

    # 子页面中找div标签中class = "article"的区域，再在此区域找img标签
    child_img = child_page.find("div", attrs={"class" : "article"}).find("img")
    # print(child_img.get("src"))

    child_src = child_img.get("src")# 在img标签中找src属性的值
    img_resp = requests.get(child_src)# 访问图片src的网页
    
    i = "picture.jpg"
    img_name = "第" + str(cnt) + "张" + i
    cnt += 1

    with open(img_name, mode="wb") as f :
        f.write(img_resp.content)# 通过字节形式下载图片

    print("over!!!" + img_name)
    time.sleep(2)

print("all over!!!")
