from multiprocessing import Process
import time

def f(i):
    time.sleep(1)
    print('hello world', i)

if __name__ == '__main__':
    for num in range(10):
        Process(target=f, args=(num,)).start()