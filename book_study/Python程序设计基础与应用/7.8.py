from pypinyin import lazy_pinyin, pinyin

print(lazy_pinyin('董付国')) # 拼音
print(lazy_pinyin('董付国', 1)) # 带声调的拼音
print(lazy_pinyin('董付国', 2)) # 用数字表示声调
print(lazy_pinyin('董付国', 3)) # 拼音首字母

# 多音字
print(lazy_pinyin('重要', 1))
print(lazy_pinyin('重阳', 1))
print(pinyin('重阳'))
print(pinyin('重阳节', heteronym=True))

# ['dong', 'fu', 'guo']
# ['dǒng', 'fù', 'guó']
# ['do3ng', 'fu4', 'guo2']
# ['d', 'f', 'g']
# ['zhòng', 'yào']
# ['chóng', 'yáng']
# [['chóng'], ['yáng']]
# [['chóng'], ['yáng'], ['jié', 'jiē']]
