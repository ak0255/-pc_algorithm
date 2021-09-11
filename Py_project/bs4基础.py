import requests
from bs4 import BeautifulSoup

url = "https://movie.douban.com/chart"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36"
}

resp = requests.get(url, headers=headers)

# print(resp.text)
page = BeautifulSoup(resp.text, "html.parser")

div = page.find("div", attrs={"class":"global-nav-items"})
# print(div)
lis = div.find_all("li")

print(lis[0].text)

# for i in lis :
#     a = i.find_all("a")
#     print(a[0].text)
#     print('-' * 30)
