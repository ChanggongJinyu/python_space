a = 4.2
b = 2.1
print(a+b,len(str(a + b)))
# 6.300000000000001 17
# 这个误差实际上是底层CPU的浮点运算单元和IEEE 754浮点数算术标准的一种“特性”。
# float 提供17位的精度

# 如果期望得到更高的精度（并愿意牺牲一些性能），可以使用decimal模块
from decimal import Decimal
a = Decimal('4.2')
b = Decimal('2.1')
print(a + b)
print((a + b) == Decimal('6.3'))
# 6.3
# True

# decimal模块的主要功能是允许控制计算过程中的各个方面，包括数字的位数和四舍五入
from decimal import localcontext
a = Decimal('1.3')
b = Decimal('1.7')
print(a/b) #0.7647058823529411764705882353
with localcontext() as ctx:
    ctx.prec = 3
    print(a/b) # 0.765

# 还需注意相减抵消以及大数加小数的情况
nums = [1.23e+18,1,-1.23e+18]
print(sum(nums))
# 0.0
import math
print(math.fsum(nums))
# 1.0

# decimal模块主要用在涉及金融这一类业务的程序中。