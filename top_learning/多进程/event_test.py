import time
import random
from multiprocessing import Process, Event

def now():
    return str(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))

def traffic_light(e):
    print(now() + ' \033[31m红灯亮\033[0m')  # 标识默认是False，代表红灯
    while True:
        if e.is_set():  # 如果是绿灯(标识是为True)
            time.sleep(2)  # 2秒后
            print(now() + ' \033[31m红灯亮\033[0m')  # 转为红灯
            e.clear()  # 设置为False

        else:  # 如果是红灯
            time.sleep(2)  # 2秒后
            print(now() + ' \033[32m绿灯亮\033[0m')  # 转为绿灯
            e.set()  # 设置为True

def people(e, i):
    if not e.is_set(): #如果红灯(标识为False)
        print(now() + ' people %s 在等待' % i)
        e.wait() #行人等待，直到绿灯(即标识为True)
    print(now() + ' people %s 通过了' % i)

if __name__ == '__main__':
    e = Event()  # 默认为 False，红灯亮
    p = Process(target=traffic_light, args=(e,))  # 红绿灯进程
    p.daemon = True
    p.start()
    process_list = []
    for i in range(6):  # 6人过马路
        time.sleep(random.randrange(0, 4, 2))
        p = Process(target=people, args=(e, i))
        p.start()
        process_list.append(p)

    for p in process_list:
        p.join()