# 实现优先级队列
# 以给定的优先级对元素排序，且每次pop操作时都会返回优先级最高的那个元素

import heapq

class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self,item,priority):
        # priority取负是让队列能够按照元素的优先级从高到低的顺序排列
        # index的作用是为了将具有相同优先级的元素以适当的顺序排列
        heapq.heappush(self._queue,(-priority, self._index, item))
        self._index += 1
        print(self._queue)

    def pop(self):
        return heapq.heappop(self._queue)[-1]


class Item:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return 'Item({!r})'.format(self.name)


q = PriorityQueue()
q.push(Item('foo'),1)
q.push(Item('bar'), 5)
q.push(Item('spam'), 4)
q.push(Item('grok'), 1)
# 优先级相同的2个元素(foo,grok)返回的顺序同它们插入到队列时的顺序相同

print("Should be bar:", q.pop())
print("Should be spam:", q.pop())
print("Should be foo:", q.pop())
print("Should be grok:", q.pop())