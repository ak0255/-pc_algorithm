import requests
import re

domain = "https://www.dytt89.com/"
resp = requests.get(domain)  # verify=False 取消安全验证
resp.encoding = 'gb2312'

# with open("电影天堂首页.html", "w") as f :
#     f.write(resp.text)

# print(resp.text)

obj1 = re.compile(r"2021必看热片.*?<ul>(?P<ul>.*?)</ul>", re.S)
obj2 = re.compile(r"<a href='(?P<href>.*?)'", re.S)
obj3 = re.compile(r'<td style="WORD-WRAP: break-word" bgcolor="#fdfddf"><a href="(?P<download>.*?)">', re.S)

result1 = obj1.finditer(resp.text)
child_href_list = []

for it in result1:
    ul = it.group('ul')
    # 拿到<li>标签中的内容
    # print(ul)

    result2 = obj2.finditer(ul)

    for itt in result2:
        # 拿到子页面的拓展url，相加得到子页面的url
        child_href = domain + itt.group('href').strip("/")
        child_href_list.append(child_href)
        # print(itt.group('href'))

#存入txt中需要转换成utf-8来存储，否则乱码
f = open('电影天堂2021必看.txt', mode='a', encoding='utf-8')
# 提取子页面内容
for href in child_href_list:
    child_resp = requests.get(href)
    child_resp.encoding = 'gb2312'
    # print(child_resp.text)

    result3 = obj3.search(child_resp.text)
    # print(result3.group('download'))
    # print('-' * 30)

    f.write(result3.group('download') + '\n')
    f.write('-' * 30 + '\n')

f.close()
    
