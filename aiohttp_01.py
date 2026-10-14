# async就相当于声明：“啊这里有个协程，你可以用await把它挂起然后干别的事”
# 正常情况下，程序会等A弄完再弄B，挂起的意思就是让B不要等A了

import asyncio
import aiohttp

urls = [
    "https://wallpapercave.com/wp/JhBfVjJ.jpg",
    "https://wallpapercave.com/wp/fNvE9eV.jpg",
    "https://wallpapercave.com/wp/Fl83heL.jpg"
]

async def aiodownload(url):
    name = url.split("/")[-1]
    # 发送请求
    # 得到图片内容
    # 保存到文件
    async with aiohttp.ClientSession() as session:   # 等价requests，aiohttp.ClientSession()是一个上下文管理器
        async with session.get(url) as resp:         # requests.get(url)  ->  session.get(url)   #  requests.get()是一个阻塞的函数，aiohttp.ClientSession().get()是一个协程对象
            with open(name, mode="wb") as f:
                # 这里可以自学aiofiles，aiofiles是一个异步文件操作库，可以让你在异步环境中进行文件读写操作，不会阻塞事件循环         
                f.write(await resp.content.read())   # 等价于原来的resp.content()
        

async def main():
    tasks = []
    for url in urls:
        tasks.append(aiodownload(url))

    await asyncio.gather(*tasks)    # gather的作用是把多个协程任务包装成一个协程对象，等这个对象完成了，说明所有的任务都完成了
    # 新版的python不再接受协程对象了，必须是任务对象，所以要用asyncio.create_task()把协程对象转换成任务对象

if __name__ == "__main__":
    asyncio.run(main())