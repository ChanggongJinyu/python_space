s = 'p\xfdt\u0125\xf6\xf1\x0cis\tawesome\r\n'
# print(s)

s = 'pyt\u0125on\x0cis\tawesome\r\n'
print(s)

remap = {
    ord('\t') : ' ',
    ord('\f') : ' ',
    ord('\r') : None      # Deleted
}
# ord() 函数是 chr() 函数（对于8位的ASCII字符串）或 unichr() 函数（对于Unicode对象）的配对函数，
# 它以一个字符（长度为1的字符串）作为参数，返回对应的 ASCII 数值，或者 Unicode 数值
print('ord("\t")', ord('\t'), 'ord("\f")', ord('\f'), 'ord("\r")', ord('\r'))
a = s.translate(remap)
print(a)

import unicodedata,sys
print(sys.maxunicode) #1114111
# 判断c是否为组合字符
cmb_chrs = dict.fromkeys(c for c in range(sys.maxunicode) if unicodedata.combining(chr(c)))
print(cmb_chrs)
b = unicodedata.normalize('NFD',a)
print(b)
print(b.translate(cmb_chrs))

# 将十进制数字字符映射为对应的ascii版本
digitmap = {c: ord('0') + unicodedata.digit(chr(c)) for c in range(sys.maxunicode) if unicodedata.category(chr(c)) == 'Nd'}
# unicodedata.category返回字符在unicode里分类的类型
# 'Nd' 表示 number, decimal digit
# unicodedata.digit() 把一个合法的数字字符串转换为数字值
print(digitmap)
x = '\u0661\u0662\u0663'
print(x.translate(digitmap))

print(b.encode('ascii','ignore').decode('ascii'))