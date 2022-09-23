from multiprocessing import Pool
import time
import random

def f(x):
    # print('子进程开始', x, time.ctime(time.time()))
    time.sleep(random.randint(1, 5))
    res = x * x
    # print(res)
    return res

def res_callback(res):
    print(res)

if __name__ == '__main__':
    with Pool(processes=4) as pool:
        res_list = []
        for i in range(10):
            pool.apply_async(f, (i,), callback=res_callback)
        pool.close() # 关闭进程池，阻止新的进程进入
        pool.join() # 主进程阻塞，直到进程池里的任务全部结束
