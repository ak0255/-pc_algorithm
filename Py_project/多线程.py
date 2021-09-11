'''
from threading import Thread

class MyThread(Thread) :
    def run(self):
        for i in range(1000) :
            print("------", i)


def func() :
    for i in range(100) :
        print("func---", i)

if __name__ == "__main__" :
    
    t = MyThread()
    t.start()

    for i in range(100) :
        print("main",i)
        
'''

from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

def funf(name) :
    for i in range(1000) :
        print(name, i)


if __name__ == "__main__" :
    with ThreadPoolExecutor(50) as f :
        for i in range(100) :
            f.submit(funf, name = f"线程{i}",)