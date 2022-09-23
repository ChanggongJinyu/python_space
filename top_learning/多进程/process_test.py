from multiprocessing import Process
import time

def add(x, y):
    print('开始函数add')
    result = x + y
    time.sleep(1)
    print('结束函数add',result)

def subtraction(x, y):
    print('开始函数subtraction')
    result = x - y
    time.sleep(2)
    print('结束函数subtraction',result)

if __name__ == '__main__':
    a = Process(target=add,args=(10, 5), name='加法')
    s = Process(target=subtraction, args=(10, 5), name='减法')

    a.start()
    s.start()
    a.join()
    s.join()

    print('End')