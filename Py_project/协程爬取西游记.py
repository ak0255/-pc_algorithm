# https://dushu.baidu.com/api/pc/getCatalog?data={"book_id":"4306063500"}
# https://dushu.baidu.com/api/pc/getChapterContent?data={"book_id":"4306063500","cid":"4306063500|11348571","need_bookinfo":1}

import requests
import aiohttp
import asyncio
import aiofiles
import json
import time


async def download(title, cid, b_id):
    data = {
        "book_id": b_id,
        "cid": f"{b_id}|{cid}",
        "need_bookinfo": 1
        }
    data = json.dumps(data)

    url = "https://dushu.baidu.com/api/pc/getChapterContent?data=" + data

    async with aiohttp.ClientSession() as session :
        async with session.get(url) as resp :
            dict = await resp.json()
            async with aiofiles.open("E:\VS\Py_Project\数据存储\西游记100话\\" + title, mode="w", encoding="utf-8") as f :
                await f.write(dict['data']['novel']['content'])

    pass


async def getCatalog(url):
    resp = requests.get(url)
    # print(resp.text)
    dict = resp.json()
    tasks = []
    for item in dict['data']['novel']['items']:
        title = item['title']
        cid = item['cid']
        tasks.append(download(title, cid, book_id))
        # break
        # print(title, cid)
    await asyncio.wait(tasks)
    pass

if __name__ == "__main__":
    t1 = time.time()
    book_id = "4306063500"
    url = 'https://dushu.baidu.com/api/pc/getCatalog?data={"book_id":"' + book_id + '"}'
    loop = asyncio.get_event_loop()
    loop.run_until_complete(getCatalog(url))
    t2 = time.time()
    print(t2 - t1)
