# 拿到页面源代码 requests
# 利用re来提取信息 re
import requests
import re
import csv

# url = "https://movie.douban.com/top250"
# header = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36"
# }
# resp = requests.get(url, headers=header)
# # 源代码
# # with open("top250前25.html", "w", encoding="utf-8") as f :
# #     f.write(resp.text)

# #源代码变量
# page_content = resp.text

# obj = re.compile(r'<div class="info">.*?<span class="title">(?P<name>.*?)</span>'
#                 +r'.*?<br>(?P<year>.*?)&nbsp'
#                 +r'.*?"v:average">(?P<score>.*?)</span>'
#                 +r'.*?<span>(?P<number>.*?)人评价</span>', re.S)

# it = obj.finditer(page_content)

# for i in it :
#     print("电影名称 ：" + i.group("name"))
#     print("电影上映年份 ：" + i.group("year").strip())
#     print("电影的评分 ：" + i.group("score"))
#     print("电影的评价人数 ：" + i.group("number"))
#     print("-" * 30)


def get(url):
    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36"
    }
    resp = requests.get(url, headers=header)
    page_content = resp.text
    obj = re.compile(r'<div class="info">.*?<span class="title">(?P<name>.*?)</span>'
                     + r'.*?<br>(?P<year>.*?)&nbsp'
                     + r'.*?"v:average">(?P<score>.*?)</span>'
                     + r'.*?<span>(?P<number>.*?)人评价</span>', re.S)
    it = obj.finditer(page_content)

    try:
        # 新的一行默认回车，newline=""可以使新一行没有内容
        f = open('豆瓣top250信息.csv', mode='a', encoding="utf-8", newline="")
        csvwriter = csv.writer(f)
    except:
        print('打开文件失败')

    for i in it:
        dic = i.groupdict()
        dic['year'] = dic['year'].strip()
        csvwriter.writerow(dic.values())
    f.close()
'''txt文件存储数据
    for i in it :
        with open('top250.txt', 'a', encoding='utf-8') as f :
            f.write("电影名称 ：" + i.group("name") + '\n')
            f.write("电影上映年份 ：" + i.group("year").strip() + '\n')
            f.write("电影的评分 ：" + i.group("score") + '\n')
            f.write("电影的评价人数 ：" + i.group("number") + '\n')
            f.write("-" * 30 + '\n')
'''
def main():
    for s in range(10):
        url = "https://movie.douban.com/top250?start=" + str(s * 25)
        get(url)


if __name__ == "__main__":
    main()
