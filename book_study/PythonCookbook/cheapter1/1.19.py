nums = [1, 2, 3, 4, 5]
print(sum(x * x for x in nums))
# 生成器表达式
print(sum((x * x for x in nums)))