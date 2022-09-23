# 冒泡排序算法turtle演示

from turtle import *
from random import randint

class Block(Turtle):
    def __init__(self, size):
        self.size = size
        Turtle.__init__(self, shape="square", visible=False)
        self.pu() # 画笔抬起
        self.shapesize(size * 1.5, 1.5, 2) # square-->rectangle
        self.fillcolor("black")
        self.st() # 显示海龟

    def glow(self):
        self.fillcolor("red")

    def unglow(self):
        self.fillcolor("black")

class Shelf(list):
    def __init__(self, y):
        "create a shelf. y is y-position of first block"
        self.y = y
        self.x = -150

    def push(self, d):
        width, _, _ = d.shapesize()
        # align blocks by the bottom edge
        y_offset = width / 2 * 20
        d.sety(self.y + y_offset)
        d.setx(self.x + 34 * len(self))
        self.append(d)

    def pop(self, key):
        b = list.pop(self, key)
        print(b)
        b.glow()
        b.sety(200)
        self._close_gap_from_i(key)
        return b

    def _close_gap_from_i(self, i):
        for b in self[i:]:
            xpos, _ = b.pos()
            b.setx(xpos - 34)

    def _open_gap_from_i(self, i):
        for b in self[i:]:
            xpos, _ = b.pos()
            b.setx(xpos + 34)

    def insert(self, key, b):
        self._open_gap_from_i(key)
        list.insert(self, key, b)
        b.setx(self.x + 34 * key)
        width, _, _ = b.shapesize()
        # align blocks by the bottom edge
        y_offset = width / 2 * 20
        b.sety(self.y + y_offset)
        b.unglow()

def show_text(text, line=0):
    line = 20 * line
    goto(0,-250 - line)
    write(text, align="center", font=("Courier", 16, "bold"))

def play():
    onkey(None, "space")
    clear()
    length = len(s)
    print(length)
    for i in range(0, length):
        flag = False
        for j in range(0, length - i - 1):
            exp = 's[j].size > s[j+1].size'  # 升序
            # if reverse:
            #     exp = 'lst[j] < lst[j+1]'  # 降序
            hole = j + 1
            if eval(exp):
                s.insert(hole, s.pop(j))
                flag = True
                if not flag:
                    break

def main():
    lst = [ randint(1, 10) for i in range(5) ]
    print(lst)

    getscreen().clearscreen()
    ht();
    penup()

    global s
    s = Shelf(-200)
    for one in lst:
        s.push(Block(one))

    write("press spacebar to start sort",
          align="center", font=("Courier", 16, "bold"))

    onkey(play, "space")
    listen()



if __name__=="__main__":
    main()
    mainloop()