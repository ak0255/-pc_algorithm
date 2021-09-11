# import requests
# import re
# import xlwt

# from requests.api import head


# def get(url, cnt):

#     cnt += 1

#     headers = {
#         "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36"
#     }
#     resp = requests.get(url, headers=headers)
#     # print(resp)
#     page = resp.text
#     obj1 = re.compile(r'<img width="100" alt="(?P<name>.*?)" src="(?P<picture_link>.*?)".*?'
#                       + r'导演: (?P<director>.*?)&nbsp.*?主演: (?P<actor>.*?)<br>(?P<year>.*?)&nbsp;/&nbsp;'
#                       + r'(?P<countries>.*?)&nbsp;/&nbsp;.*?"v:average">(?P<average>.*?)</span>.*?<span>(?P<number>\d+)人评价</span>'
#                       + r'.*?<span class="inq">(?P<summary>.*?)</span>', re.S)
#     #正则提取有问题！！！！！！！！！！！！！！！！！！！！！！！！
#     it = obj1.finditer(page)

#     for i in it :
#         dic = i.groupdict()
#         dic['year'] = dic['year'].strip()
#         values_list = list(dic.values())
#         for j in range(9) :
#             worksheet.write(cnt, j, values_list[j])
#         # break
#         print("第%d条over！"%cnt)
#         cnt += 1
#     pass


# def main():
#     for s in range(10):
#         url = "https://movie.douban.com/top250?start=" + str(s * 25)
#         get(url, s * 25)
#         print("已完成第%d页信息的爬取"%(s + 1))
#         # break


# if __name__ == "__main__":
#     workbook = xlwt.Workbook(encoding="utf-8")
#     worksheet = workbook.add_sheet('My Worksheet')
#     label = ('电影名称','图片链接','导演','主演','年份','国家','评分','评价人数','概括')
#     for i in range(9) :
#         worksheet.write(0, i, label[i])
#     main()
#     print("保存完成!!!")
#     workbook.save("豆瓣250.xls")



import requests
import re
import xlwt
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor


def get(child_url, cnt):

    cnt += 1

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36"
    }
    resp = requests.get(child_url, headers=headers)
    # print(resp)
    page = resp.text
    
    soup = BeautifulSoup(page, 'html.parser')

    for i in soup.find_all("div", attrs={"class" : "item"}) :
        # print(i)
        datas = []

        img = i.find("img")
        name = img.get("alt")
        img_src = img.get("src")

        some_div = i.find("div", attrs={"class" : "bd"})
        p = some_div.find("p")
        p = str(p.text).strip()

        # print(p.split('\n')[0])
        # print('-' * 30)
        # print(p.split('\n')[1])

        if "主演: " in p :
            director = p.split("主演: ")[0].strip("导演: ")
        else :
            director = p.split('\n')[0].strip("导演: ")

        if "主演: " in p :
            actor = p.split("主演: ")[1].split('\n')[0]
        else :
            actor = ""

        year = p.split('\n')[1].split('/')[0].strip()
        countries = p.split('\n')[1].split('/')[1].strip()
        type = p.split('\n')[1].split('/')[2].strip()

        i = str(i)
        main_url = re.findall(findmain_url, i)[0]
        average = re.findall(findaverage, i)[0]
        number = re.findall(findnumber, i)[0]
        if "inq" in i :
            summary = re.findall(findsummary, i)[0]
        else :
            summary = ""

        datas.append(main_url)   # 主页地址
        datas.append(name)       # 电影名称
        datas.append(img_src)    # 图片地址
        datas.append(director)   #导演
        datas.append(actor)      #主演
        datas.append(year)       #年份
        datas.append(countries)  #国家
        datas.append(type)       #类型
        datas.append(average)    #评分
        datas.append(number)     #评价人数
        datas.append(summary)    #概括

        # for data in datas :
        #     print(data)

        # 写入文件
        for j in range(11) :
            worksheet.write(cnt, j, datas[j])
        # print(main_url)
        # print(name)
        # print(img_src)
        # print(director)
        # print(actor)
        cnt += 1
        # break

findmain_url = re.compile(r'<a href="(.*?)">', re.S)
findaverage = re.compile(r'<span class="rating_num" property="v:average">(.*?)</span>', re.S)
findnumber = re.compile(r'<span>(\d*)人评价</span>', re.S)
findsummary = re.compile(r'<span class="inq">(.*?)</span>', re.S)


def main():
    with ThreadPoolExecutor(10) as t :# 多线程爬取
        for s in range(10):
            url = "https://movie.douban.com/top250?start=" + str(s * 25)
            # get(url, s * 25)
            t.submit(get, child_url = url, cnt = s * 25)
            print("已完成第%d页信息的爬取"%(s + 1))
            # break


if __name__ == "__main__":
    workbook = xlwt.Workbook(encoding="utf-8")
    worksheet = workbook.add_sheet('My Worksheet')
    label = ('主页链接','电影名称','图片链接','导演','主演','年份','国家','类型','评分','评价人数','概括')
    for i in range(11) :
        worksheet.write(0, i, label[i])
    main()
    print("保存完成!!!")
    workbook.save("豆瓣250.xls")
