#!/usr/bin/env python3
"""

         sorting_animation.py

A minimal sorting algorithm animation:
Sorts a shelf of 10 blocks using insertion
sort, selection sort and quicksort.

Shelfs are implemented using builtin lists.

Blocks are turtles with shape "square", but
stretched to rectangles by shapesize()
 ---------------------------------------
       To exit press space button
 ---------------------------------------
"""
from turtle import *
import random


class Block(Turtle):

    def __init__(self, size):
        self.size = size
        Turtle.__init__(self, shape="square", visible=False) # visible 是否可见
        self.pu() # 抬起画笔
        self.shapesize(size * 1.5, 1.5, 2) # square-->rectangle
        # 设置画笔的属性 x/y-拉伸因子和/或轮廓
        self.fillcolor("black")
        self.st() #showturtle() 显示海龟

    def glow(self):
        self.fillcolor("red") # 弹出元素时填充颜色为红色

    def unglow(self):
        self.fillcolor("black") # 插入元素时填充颜色为黑色

    def __repr__(self):
        return "Block size: {0}".format(self.size)

 # 继承list
class Shelf(list):

    def __init__(self, y):
        "create a shelf. y is y-position of first block"
        self.y = y
        self.x = -150

    # 将Block移动到某个位置
    def push(self, d):
        width, _, _ = d.shapesize()
        # align blocks by the bottom edge
        y_offset = width / 2 * 20
        d.sety(self.y + y_offset)
        d.setx(self.x + 34 * len(self))
        self.append(d)

    def _close_gap_from_i(self, i):
        for b in self[i:]:
            xpos, _ = b.pos() # 位置
            b.setx(xpos - 34) # 弹出一个Block后，其他Block依次向左移动

    def _open_gap_from_i(self, i):
        for b in self[i:]:
            xpos, _ = b.pos()
            b.setx(xpos + 34) # 弹出一个Block后，其他Block依次向右移动

    def pop(self, key):
        b = list.pop(self, key) # 弹出索引key表示的元素
        b.glow()
        b.sety(200)
        self._close_gap_from_i(key)
        return b

    def insert(self, key, b):
        self._open_gap_from_i(key)
        list.insert(self, key, b)
        b.setx(self.x + 34 * key)
        width, _, _ = b.shapesize()
        # align blocks by the bottom edge
        y_offset = width / 2 * 20
        b.sety(self.y + y_offset)
        b.unglow()

# 插入法排序
def isort(shelf):
    length = len(shelf)
    for i in range(1, length):
        hole = i
        while hole > 0 and shelf[i].size < shelf[hole - 1].size:
            hole = hole - 1
        shelf.insert(hole, shelf.pop(i))
    return

# selection sort 选择法排序
def ssort(shelf):
    length = len(shelf)
    for j in range(0, length - 1):
        # 假设剩余元素中第一个最小
        imin = j
        # 扫描剩余元素
        for i in range(j + 1, length):
            # 如果有更小的，就记录下它的位置
            if shelf[i].size < shelf[imin].size:
                imin = i
        # imin保存的是最小的元素的索引
        if imin != j:
            shelf.insert(j, shelf.pop(imin))

def bsort(shelf):
    length = len(shelf)
    for i in range(0, length):
        flag = False
        for j in range(0, length - i - 1):
            if shelf[j].size > shelf[j+1].size:
                hole = j + 1
                shelf.insert(hole, shelf.pop(j))
                flag = True
                if not flag:
                    break

def partition(shelf, left, right, pivot_index):
    pivot = shelf[pivot_index]
    shelf.insert(right, shelf.pop(pivot_index))
    store_index = left
    for i in range(left, right): # range is non-inclusive of ending value
        if shelf[i].size < pivot.size:
            shelf.insert(store_index, shelf.pop(i))
            store_index = store_index + 1
    shelf.insert(store_index, shelf.pop(right)) # move pivot to correct position
    return store_index

# quicksort 快排
def qsort(shelf, left, right):
    if left < right:
        pivot_index = left
        pivot_new_index = partition(shelf, left, right, pivot_index)
        qsort(shelf, left, pivot_new_index - 1)
        qsort(shelf, pivot_new_index + 1, right)

def randomize():
    disable_keys()
    clear()
    target = list(range(10))
    random.shuffle(target)
    for i, t in enumerate(target):
        for j in range(i, len(s)):
            if s[j].size == t + 1:
                s.insert(i, s.pop(j))
    show_text(instructions1)
    show_text(instructions2, line=1)
    enable_keys()

def show_text(text, line=0):
    line = 20 * line
    goto(0,-250 - line) # 前往某个位置
    write(text, align="center", font=("Courier", 16, "bold")) # 书写

def start_ssort():
    disable_keys()
    clear()
    show_text("Selection Sort")
    ssort(s)
    clear()
    show_text(instructions1)
    show_text(instructions2, line=1)
    enable_keys()

def start_isort():
    disable_keys()
    clear() # 清空
    show_text("Insertion Sort")
    isort(s)
    clear()
    show_text(instructions1)
    show_text(instructions2, line=1)
    enable_keys()

def start_qsort():
    disable_keys()
    clear()
    show_text("Quicksort")
    qsort(s, 0, len(s) - 1)
    clear()
    show_text(instructions1)
    show_text(instructions2, line=1)
    enable_keys()

# 冒泡排序Bubble Sort
def start_bsort():
    disable_keys()
    clear()
    show_text("Bubble Sort")
    bsort(s)
    clear()
    show_text(instructions1)
    show_text(instructions2, line=1)
    enable_keys()

# 准备好10个长方形海龟
def init_shelf():
    global s
    s = Shelf(-200)
    vals = (4, 2, 8, 9, 1, 5, 10, 3, 7, 6)
    for i in vals:
        s.push(Block(i))

def disable_keys():
    onkey(None, "s") # 按键释放
    onkey(None, "i")
    onkey(None, "q")
    onkey(None, "b")
    onkey(None, "r")

def enable_keys():
    onkey(start_isort, "i") # 绑定 fun 指定的函数到按键释放事件。 绑定 fun 指定的函数到按键释放事件
    onkey(start_ssort, "s")
    onkey(start_qsort, "q")
    onkey(start_bsort, "b")
    onkey(randomize, "r")
    onkey(bye, "space") # bye() 退出

def main():
    getscreen().clearscreen() # getscreen()获取屏幕；clearscreen()删除所有海龟的全部绘图
    ht() # hideturtle()隐藏海龟
    penup() # 抬起画笔
    init_shelf()
    show_text(instructions1)
    show_text(instructions2, line=1)
    enable_keys()
    listen() # 设置焦点到 TurtleScreen (以便接收按键事件)。
    return "EVENTLOOP"

instructions1 = "press i for insertion sort, s for selection sort, q for quicksort,\n b for bubble sort"
instructions2 = "spacebar to quit, r to randomize"

if __name__=="__main__":
    msg = main()
    mainloop()
#     开始事件循环 - 调用 Tkinter 的 mainloop 函数。必须作为一个海龟绘图程序的结束语句。
#     如果一个脚本是在以 -n 模式 (无子进程) 启动的 IDLE 中运行时 不可 使用 - 用于实现海龟绘图的交互功能。
