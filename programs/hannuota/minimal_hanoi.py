#!/usr/bin/env python3
"""       turtle-example-suite:

         tdemo_minimal_hanoi.py

A minimal 'Towers of Hanoi' animation:
A tower of 6 discs is transferred from the
left to the right peg.

An imho quite elegant and concise
implementation using a tower class, which
is derived from the built-in type list.

Discs are turtles with shape "square", but
stretched to rectangles by shapesize()
 ---------------------------------------
       To exit press STOP button
 ---------------------------------------
"""
from turtle import *

# 继承Turtle类
# 设置长方形的长，宽，填充色
class Disc(Turtle):
    def __init__(self, n):
        Turtle.__init__(self, shape="square", visible=False)
        # 继承父类的构造方法，也可以写成：super(Disc,self).__init__(shape="square", visible=False)
        # 即初始化父类
        self.pu() # 画笔抬起
        self.shapesize(1.5, n*1.5, 2) # square-->rectangle
        # 设置画笔的属性，参数(stretch_wid, stretch_len, outline)
        # stretch_wid 为垂直于其朝向的宽度拉伸因子
        # stretch_len 为平等于其朝向的长度拉伸因子
        # outline 决定形状轮廓线的粗细。
        self.fillcolor(n/6., 0, 1-n/6.) # 填充颜色
        self.st() # 显示海龟

class Tower(list):
    "Hanoi tower, a subclass of built-in type list"
    def __init__(self, x):
        "create an empty tower. x is x-position of peg"
        print(self)
        self.x = x
    # 将图形固定在某个位置
    def push(self, d):
        d.setx(self.x) # 设置海龟的横坐标
        print(len(self))
        print(-150+34*len(self))
        d.sety(-150+34*len(self)) # 设置海龟的纵坐标
        self.append(d)
    def pop(self):
        d = list.pop(self)
        d.sety(150)
        return d

def hanoi(n, from_, with_, to_):
    if n > 0:
        hanoi(n-1, from_, to_, with_)
        to_.push(from_.pop())
        hanoi(n-1, with_, from_, to_)

def play():
    onkey(None,"space")
    clear()
    # 从屏幕中删除指定海龟的绘图。不移动海龟。海龟的状态和位置以及其他海龟的绘图不受影响。
    try:
        hanoi(n_floors, t1, t2, t3)
        # write("press STOP button to exit",
        #       align="center", font=("Courier", 16, "bold"))
    except Terminator:
        pass  # turtledemo user pressed STOP

def main():
    global t1, t2, t3
    ht(); penup();
    goto(0, -225)   # writer turtle
    speed('slowest')
    # ht() 隐藏海龟
    # penup() 抬起画笔
    # goto() 移动
    t1 = Tower(-250)
    t2 = Tower(0)
    t3 = Tower(250)
    # make tower of 6 discs
    for i in range(n_floors,0,-1):
        t1.push(Disc(i))
    # prepare spartanic user interface ;-)
    write("press spacebar to start game",
          align="center", font=("Courier", 16, "bold"))
    # turtle.write(arg, move=False, align='left', font=('Arial', 8, 'normal'))
    # arg, 要书写到 TurtleScreen 的对象
    onkey(play, "space")
    # onkey(fun, key)
    # 绑定 fun 指定的函数到按键释放事件
    # 如果 fun 值为 None，则移除事件绑定。
    listen()
    # 监听
    return "EVENTLOOP"

if __name__=="__main__":
    global n_floors
    n_floors = 6
    msg = main()
    print(msg)
    mainloop()
    # 开始事件循环 - 调用 Tkinter 的 mainloop 函数
    # 必须作为一个海龟绘图程序的结束语句。
    # 如果一个脚本是在以 -n 模式 (无子进程) 启动的 IDLE 中运行时 不可 使用 - 用于实现海龟绘图的交互功能