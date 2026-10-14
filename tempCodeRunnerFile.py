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

if __name__ == "__main__":
    f1 = func1()
    f2 = func2()
    f3 = func3()
    task = [f1, f2, f3]

    asyncio.run(asyncio.wait(task))