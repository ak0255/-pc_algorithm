# import requests

# url = 'http://maoyan.com/board/4'
# rs = requests.get(url)
# print(rs.text)
import json
import requests
from requests.exceptions import RequestException  # 引入异常
import re
import time


def get_one_page(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:  # 由状态码判断返回结果
            return response.text  # 返回网页内容
        return None
    except RequestException:
        return None


def parse_one_page(html):
    pattern = re.compile('<dd>.*?board-index.*?>(\d+)</i>.*?data-src="(.*?)".*?name"><a'
                         + '.*?>(.*?)</a>.*?star">(.*?)</p>.*?releasetime">(.*?)</p>'
                         + '.*?integer">(.*?)</i>.*?fraction">(.*?)</i>.*?</dd>', re.S)  # compile函数表示一个方法对象，re.s匹配多行
    items = re.findall(pattern, html)  # 以列表形式返回全部能匹配的字符串。
    for item in items:  # 将结果以字典形式返回键值对
        yield {  # 把这个方法变成一个生成器
            'index': item[0],
            'image': item[1],
            'title': item[2],
            'actor': item[3].strip()[3:],
            'time': item[4].strip()[5:],
            'score': item[5] + item[6]  # 将评分整数和小数结合起来
        }


def write_to_file(content):
    with open('result.txt', 'a', encoding='utf-8') as f:  # 将结果写入文件
        f.write(json.dumps(content, ensure_ascii=False) + '\n')


def main(offset):
    url = 'http://maoyan.com/board/4?offset=' + str(offset)
    html = get_one_page(url)
    for item in parse_one_page(html):
        # print(item)
        write_to_file(item)


if __name__ == '__main__':
    for i in range(10):
        main(offset=i * 10)
        time.sleep(1)
