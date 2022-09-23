data = b'\x00\x124V\x00x\x90\xab\x00\xcd\xef\x01\x00#\x004'
print(len(data))
print(int.from_bytes(data,'little'),int.from_bytes(data,'big'))
# 69120565665751139577663547927094891008 94522842520747284487117727783387188
# 如果byteorder为'big'，则最重要的字节位于字节数组的开头。 如果byteorder为'little'，则最重要的字节位于字节数组的末尾。

x = 94522842520747284487117727783387188
print(x.to_bytes(16,'big'),x.to_bytes(16,'little'))
# b'\x00\x124V\x00x\x90\xab\x00\xcd\xef\x01\x00#\x004' b'4\x00#\x00\x01\xef\xcd\x00\xab\x90x\x00V4\x12\x00'

# struct解包
import struct
hi,lo = struct.unpack('>QQ',data)
print(hi,lo) # 5124093560524971 57965157801984052
print((hi << 64) + lo) #94522842520747284487117727783387188

# https://blog.csdn.net/aic1999/article/details/80102433
# 一些解释
