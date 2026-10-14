
from threading import Thread      # 线程类

# def func():
#     for i in range(10):
#         print("func", i)

# if __name__ == '__main__':
#     t = Thread(target=func)       # 创建线程并安排任务
#     t.start()                     # 可以开始执行该线程，具体执行时间由CPU决定

#     for i in range(20):
#         print("main", i)

class my_thread(Thread):
    def run(self):  #线程被执行的时候，就是在执行run()
        for i in range(10):
            print(i)

if __name__ == '__main__':
    t = my_thread()
    t.start()   #t.run()不行，因为这样仍然是单线程