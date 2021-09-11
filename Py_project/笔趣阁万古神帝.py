import requests
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor
import time
# import re

headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36"
}

def downtext(url, name) :
    child_resp = requests.get(url, headers=headers)
    child_resp.encoding = "utf-8"
    # print(child_resp.text)
    # <div class="content" id="content">
    child_page = BeautifulSoup(child_resp.text, "html.parser")
    div = child_page.find("div", attrs={"id" : "content"})
    p_lists = div.find_all("p")
    with open("E:\VS\Py_Project\数据存储\笔趣阁万古神帝\\" + str(name) + ".txt", mode="a", encoding="utf-8") as f :
        for p in p_lists :
            tx = p.next_element
            f.write(tx + '\n')




            pass



    pass

def main(url) :
    resp = requests.get(url, headers=headers)
    resp.encoding = "utf-8"
    # print(resp.text) # 子页面源码
    # <ul class="section-list fix">
    page = BeautifulSoup(resp.text, "html.parser")
    dic = page.find_all("ul", attrs={"class" : "section-list fix"})[1]
    a_lists = dic.find_all_next("a")
    for a_list in a_lists :
        # print(a_list['href']) # 章节url
        child_url = a_list['href']
        name = a_list.next_element
        downtext(child_url, name)
        print(name)
        # break

    pass

if __name__ == "__main__" :
    t1 = time.time()
    with ThreadPoolExecutor(10) as t :
        for i in range(30) :
            cnt = str(i + 1)
            name = f"index_{cnt}.html"
            url =  f"https://www.changyeyuhuo.com/book/9285/{name}"
            # main(url)
            t.submit(main, url = url)
            # break
    t2 = time.time()
    print("花费了", t2 - t1, "秒")
    # 花费了 31.561957597732544 秒  600章，十个进程，感觉一般般，还是异步快

    pass