# 协程是一条线程里面不同步进行程序，与多线程有本质区别
# 异步是结合多线程使用的
import asyncio

async def func1():
    print("Alice!")
    await asyncio.sleep(3)  # 异步等三秒

async def func2():
    print("Bob!")
    await asyncio.sleep(2)

async def func3():
    print("Caroline!")
    await asyncio.sleep(4)

# 旧版python
# if __name__ == "__main__":
#     f1 = func1()
#     f2 = func2()
#     f3 = func3()
#     task = [f1, f2, f3]

#     asyncio.run(asyncio.wait(task))

# 新版python，wait不再直接接受协程对象，只接受task类型
# 可以用gather把协程对象自动包装成任务
async def main():
    # gather 会自动将协程包装成任务
    await asyncio.gather(func1(), func2(), func3())

if __name__ == "__main__":
    asyncio.run(main())