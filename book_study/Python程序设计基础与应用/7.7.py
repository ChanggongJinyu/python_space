# 中英文分词

import jieba
x = '分词的准确度直接影响了后续文本处理和挖掘算法的最终效果'
print(list(jieba.cut(x)))
# ['分词', '的', '准确度', '直接', '影响', '了', '后续', '文本处理', '和', '挖掘', '算法', '的', '最终', '效果']

print(list(jieba.cut('花纸杯'))) # ['花', '纸杯']
jieba.add_word('花纸杯')
print(list(jieba.cut('花纸杯'))) # ['花纸杯']


import snownlp
print(snownlp.SnowNLP(x).words)
# ['分词', '的', '准确度', '直接', '影响', '了', '后续', '文本', '处理', '和', '挖掘', '算法', '的', '最终', '效果']
print(snownlp.SnowNLP("花纸杯").words)
# ['花纸', '杯']
