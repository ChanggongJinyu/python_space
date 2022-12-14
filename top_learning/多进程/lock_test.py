from multiprocessing import Process, Lock
import time

def f(l, i):
    time.sleep(1)
    l.acquire()
    print('hello world', i)
    l.release()

if __name__ == '__main__':
    lock = Lock()
    for num in range(10):
        Process(target=f, args=(lock, num)).start()