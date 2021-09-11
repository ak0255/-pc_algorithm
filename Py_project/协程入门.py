'''
import asyncio
import time

async def fun1() :
    print("1")
    await asyncio.sleep(2)
    print("2")
    pass

async def fun2() :
    print("3")
    await asyncio.sleep(3)
    print("4")
    pass

async def main() :
    task = [
        fun1(),
        fun2()
    ]
    await asyncio.wait(task)
    pass

if __name__ == '__main__' :
    t1 = time.time()
    asyncio.run(main())
    t2 = time.time()
    print(t2 - t1)
    pass
'''


import asyncio
import aiohttp
import aiofiles
import time

urls = [
    "http://kr.shanghai-jiuxin.com/file/2020/1031/a2c58d6d726fb7ef29390becac5d8643.jpg",
    "http://kr.shanghai-jiuxin.com/file/2020/1031/d7de3f9faf1e0ecdea27b73139fc8d3a.jpg",
    "http://kr.shanghai-jiuxin.com/file/2020/1031/3ed27e5aedc2673755bf3327e9dcc13b.jpg",
    "http://kr.shanghai-jiuxin.com/file/2020/1031/eb2df41e2919e0b72878508ac4da08ea.jpg",
    "http://kr.shanghai-jiuxin.com/file/2020/1031/e9d17d27dfd693d88b232899538144e8.jpg",
    "http://kr.shanghai-jiuxin.com/file/2020/1031/26b7e178e987be6d914bf8d1af120890.jpg",
    "http://kr.shanghai-jiuxin.com/file/2020/1031/fdc4cc14a27eddae76d09d7c854b3496.jpg",
    "http://kr.shanghai-jiuxin.com/file/2020/0722/c4008a3a6f9853d1a6779dbe26177e32.jpg"
]

async def aiodownload(url) :
    name = url.rsplit('/', 1)[1]
    async with aiohttp.ClientSession() as session :
        async with session.get(url) as resp :
            async with aiofiles.open(name, mode='wb') as f :
                await f.write(await resp.content.read())
    print(name,'搞定')
    pass

async def main() :
    tasks = []
    for url in urls :
        d = aiodownload(url)
        tasks.append(d)
        pass
    await asyncio.wait(tasks)
    pass


if __name__ == "__main__" :
    t1 = time.time()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    t2 = time.time()
    print("用时:", t2 - t1)
    # asyncio.run(main())
