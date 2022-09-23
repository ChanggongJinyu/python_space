# 多行模式下的正则表达式

import re

comment = re.compile(r'/\*(.*?)\*/')
text1 = '/* this is a comment */'
print(comment.findall(text1))

text2 = '''/* this is a
              multiline comment */
'''
print(comment.findall(text2))
# .不能匹配换行符

comment = re.compile(r'/\*(.*?)\*/',re.DOTALL)
print(comment.findall(text2))
# re.DOTALL让.可以匹配换行符

comment = re.compile(r'/\*((?:.|\n)*?)\*/')
print(comment.findall(text2))
# (?:.|\n)指定了一个非捕获组，这个组只做匹配不捕获结果
# https://www.jianshu.com/p/2547f0e3e809