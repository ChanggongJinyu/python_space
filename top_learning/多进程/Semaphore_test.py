import time, random
from multiprocessing import Process, Semaphore

def ktv(i, sem):
    print('process {id} acquire semaphore'.format(id=i))
    sem.acquire()
    print('process {id} get semaphore do something'.format(id=i))
    time.sleep(random.randint(1, 5))
    print('process {id} release semaphore'.format(id=i))
    sem.release()

if __name__ == "__main__":
    sem = Semaphore(3)
    for i in range(10):
        p = Process(target=ktv, args=(i, sem))
        p.start()