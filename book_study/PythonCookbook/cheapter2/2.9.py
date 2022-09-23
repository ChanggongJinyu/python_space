s1 = 'Spicy Jalape\u00f1o'
s2 = 'Spicy Jalapen\u0303o'

print(s1)
print(s2)

print('s1 == s2', s1 == s2)
print(len(s1), len(s2))

# 将文本统一表示为规范形式
import unicodedata
n_s1 = unicodedata.normalize('NFC', s1)
n_s2 = unicodedata.normalize('NFC', s2)
print('n_s1 == n_s2', n_s1 == n_s2)
print(len(n_s1), len(n_s2))

t1 = unicodedata.normalize('NFD', s1)
t2 = unicodedata.normalize('NFD', s2)
print('t1 == t2', t1 == t2)
print(len(t1), len(t2))

s = '\ufb01'
print(s)
print(unicodedata.normalize('NFD',s))
print(unicodedata.normalize('NFKD',s))
print(unicodedata.normalize('NFKC',s))

for c in t1:
    # 判断是否为组合型字符
    if not unicodedata.combining(c):
        print(c)