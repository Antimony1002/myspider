from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

def fn(name):
    for i in range(100):
        print(name, i)

if __name__ == '__main__':
    with ThreadPoolExecutor(10) as t:
        for i in range(50):
            t.submit(fn, name=i)    # 给线程池提供任务

 