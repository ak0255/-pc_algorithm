import requests


def getHTMLText(url):
    proxies = {
        "https" : "https://218.244.147.59:3128"
    }
    try:
        r = requests.get(url, timeout=30, proxies=proxies)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return "产生异常"


if __name__ == "__main__":
    url = "https://www.baidu.com"
    print(getHTMLText(url))
