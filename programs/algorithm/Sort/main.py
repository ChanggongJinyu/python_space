# 冒泡排序实现

from random import randint

# 冒泡排序
def bubblesort(lst, reverse = False):
    length = len(lst)
    for i in range(0, length):
        flag = False
        for j in range(0, length -i -1):
            exp = 'lst[j] > lst[j+1]' # 升序
            if reverse:
                exp = 'lst[j] < lst[j+1]' # 降序
            if eval(exp):
                lst[j], lst[j+1] = lst[j+1], lst[j]
                print(lst)
                flag = True
                if not flag:
                    break

lst = [ randint(1, 100) for i in range(20) ]
print(lst)
bubblesort(lst)
print(lst)