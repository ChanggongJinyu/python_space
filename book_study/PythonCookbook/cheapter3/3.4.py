x = 1234
print(bin(x),oct(x),hex(x))
# 0b10011010010 0o2322 0x4d2
print(format(x,'b'),format(x,'o'),format(x,'x'))
# 10011010010 2322 4d2

print(2**32,format(2**32,'b'),format(-1234,'b'),format(2**32 - 1234,'b'))
# 100000000000000000000000000000000

# 将字符串形式的整数转换为不同的进制
print(int('4d2',16)) # 1234
print(int('10011010010',2)) # 1234