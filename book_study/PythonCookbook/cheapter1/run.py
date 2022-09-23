# 1.2 从任意长度的可迭代对象中分解元素
# *表达式
record = ['Dave','dave@example.com','773-555-1212','847-555-1212']
name, email, *phone_numbers = record
print(name,email,phone_numbers)
# Dave dave@example.com ['773-555-1212', '847-555-1212']

records = [
     ('foo', 1, 2),
     ('bar', 'hello'),
     ('foo', 3, 4),
]
def do_foo(x,y):
    print('foo', x, y)
def do_bar(s):
    print('bar', s)
for tag, *args in records:
    if tag == 'foo':
        do_foo(*args)
    elif tag == 'bar':
        do_bar(*args)
# foo 1 2
# bar hello
# foo 3 4

record = ['ACME',50,123.45,(12,18,2012)]
name, *_, (*_, year) = record
print(name,year)
# ACME 2012


# 1.3 保存最后n个元素

from collections import deque

def search(lines, pattern, history=5):
    previous_lines = deque(maxlen=history)
    for line in lines:
        if pattern in line:
            yield line, previous_lines
        previous_lines.append(line)

# Example use on a file
with open('somefile.txt') as f:
    for line, prevlines in search(f, 'python', 5):
        for pline in prevlines:
            print(pline, end='')
        print(line, end='')
        print('-'*20)


# 1.4 找到最大或最小的N个元素

import heapq

nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
print(heapq.nlargest(3,nums))
# [42, 37, 23]
print(heapq.nsmallest(3,nums))
# [-4, 1, 2]

portfolio = [
   {'name': 'IBM', 'shares': 100, 'price': 91.1},
   {'name': 'AAPL', 'shares': 50, 'price': 543.22},
   {'name': 'FB', 'shares': 200, 'price': 21.09},
   {'name': 'HPQ', 'shares': 35, 'price': 31.75},
   {'name': 'YHOO', 'shares': 45, 'price': 16.35},
   {'name': 'ACME', 'shares': 75, 'price': 115.65}
]

cheap = heapq.nsmallest(3, portfolio, key=lambda s: s['price'])
expensive = heapq.nlargest(3, portfolio, key=lambda s: s['price'])

print(cheap)
# [{'name': 'YHOO', 'shares': 45, 'price': 16.35}, {'name': 'FB', 'shares': 200, 'price': 21.09}, {'name': 'HPQ', 'shares': 35, 'price': 31.75}]
print(expensive)
# [{'name': 'AAPL', 'shares': 50, 'price': 543.22}, {'name': 'ACME', 'shares': 75, 'price': 115.65}, {'name': 'IBM', 'shares': 100, 'price': 91.1}]

print(nums)
heapq.heapify(nums) # 将list转化为堆
print(heapq.heappop(nums))
print(heapq.heappop(nums))
print(heapq.heappop(nums)) #弹出堆中第一个元素，即最小的元素，复杂度O(logN)，N代表堆的大小