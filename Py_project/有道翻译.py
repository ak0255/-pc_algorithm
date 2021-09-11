import requests
import json


def get_translate_date(word):
    url = "https://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule"
    form_data = {
        "i": word,
        "from": "AUTO",
        "to": "AUTO",
        "smartresult": "dict",
        "client": "fanyideskweb",
        "salt": "16304259539917",
        "sign": "0f5b2faa1a3b9b3c195984ee5e0a66ba",
        "lts": "1630425953991",
        "bv": "89e18957825871c419be045180c67d3b",
        "doctype": "json",
        "version": "2.1",
        "keyfrom": "fanyi.web",
        "action": "FY_BY_REALTlME"
    }
    resp = requests.post(url, data=form_data)
    # content = resp.json()
    content = json.loads(resp.text)
    print(content['translateResult'][0][0]['tgt'])


if __name__ == '__main__':
    word = input("请输入你要翻译的文字：")
    get_translate_date(word)
