# 将名称映射到序列的元素中

from collections import namedtuple
# 命名元组
# 工厂方法，返回的是元组类型的子类

Subscriber = namedtuple('Subscriber', ['addr','joined'])
sub = Subscriber('jonesy@example', '2021-10-19')
print(sub)
print(sub.addr)
print(sub.joined)

# 索引和分解
print(len(sub))
addr, joined = sub
print(addr)
print(joined)

# namedtuple的作用在于将代码同它所控制的元素位置解耦
Stock = namedtuple('Stock', ['name', 'shares', 'price'])
def compute_cost(records):
    total = 0.0
    for rec in records:
        s = Stock(*rec)
        total += s.shares * s.price
    return total
records = [
    ('GOOG', 100, 490.1),
    ('ACME', 100, 123.45),
    ('IBM', 50, 91.15)
]
print(compute_cost(records))

# 在一些情况下可以替换字典，字典需要更多的空间来存储
# 但namedtuple不可变
# 如果需要修改属性，可以使用_replace()方法，该方法会创建一个新的namedtuple
a = Stock('ACME', 100, 123.45)
print(a)
a = a._replace(shares=75)
print(a)

# _replace()可以填充具有可选或缺失字段的namedtuple
print('==============================')
Stock = namedtuple('Stock',['name','shares','price','date','time'])
stock_prototype = Stock('', 0, 0.0, None, None)
def dict_to_stock(s):
    print(s)
    return stock_prototype._replace(**s)
# **s相当于 name='ACME',shares=100,price=123.45
a = {'name': 'ACME', 'shares': 100, 'price': 123.45}
print(a)
b = dict_to_stock(a)
print(b)