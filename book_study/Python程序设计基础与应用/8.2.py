import re

example = 'Beautiful is better than ugly.'
print(re.findall('\\bb.+? \\b', example)) # 以字母b开头的完整单词
# ['better ']

print(re.findall('\\bb.+\\b', example)) # 贪心模式
# ['better than ugly']

m = re.match(r'(\w+) (\w+)', 'Isaac Newton, physicist')
print(m)
# <re.Match object; span=(0, 5), match='Isaac'>
print(m.group(0)) # Isaac Newton
print(m.group(1)) # Isaac
print(m.group(2)) # Newton
print(m.group(1,2)) # ('Isaac', 'Newton')

m = re.match(r'(?P<first_name>\w+) (?P<last_name>\w+)', 'Malcolm Reynolds') # 为子模式命名
# m = re.match(r'(\w+) (\w+)', 'Malcolm Reynolds')
print(m.group('first_name')) # Malcolm
print(m.group('last_name')) # Reynolds
print(m.groupdict()) # {'first_name': 'Malcolm', 'last_name': 'Reynolds'}

m = re.match(r'(\d+)\.(\d+)', '24.1632')
print(m.groups()) # ('24', '1632')

# 没看懂
s = 'aabc abcd abbcd abccd abcdd'
a = re.findall(r'(\b\w*(?P<f>\w+)(?P=f)\w*\b)', s)
print(a)
# [('aabc', 'a'), ('abbcd', 'b'), ('abccd', 'c'), ('abcdd', 'd')]

# 网上找的例子
exampleString = '''There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than right now.'''
pattern = re.compile(r'(?<=\w\s)never(?=\s\w)') #查找不在句子开头和结尾的never
# (?<=…) 用于正则表达式之前，如果<=后的内容在字符串中不出现则匹配，但不返回<=之后的内容
# (?=…) 用于正则表达式之后，如果=后的内容在字符串中出现则匹配，但不返回=之后的内容
# \w 匹配任意字母，数字，下划线
# \s 匹配任何空白字符，包括空格，制表符，换页符
matchResult = pattern.search(exampleString)
matchResult.span()
(172, 177)

pattern = re.compile(r'(?<=\w\s)never') #查找位于句子末尾的单词
matchResult = pattern.search(exampleString)
# matchResult.span()
# (156, 161)
# pattern = re.compile(r'(?:is\s)better(\sthan)') #查找前面是is的better than组合
# matchResult = pattern.search(exampleString)
# matchResult.span()
# (141, 155)
# matchResult.group(0)           #组0表示整个模式
# 'is better than'
# matchResult.group(1)
# ' than'
# pattern = re.compile(r'\b(?i)n\w+\b') #查找以n或N字母开头的所有单词
# index = 0
# while True:
#      matchResult = pattern.search(exampleString, index)
#  if not matchResult:
#  break
#      print(matchResult.group(0), ':', matchResult.span(0))
#      index = matchResult.end(0)
#
#
# not : (92, 95)
# Now : (137, 140)
# never : (156, 161)
# never : (172, 177)
# now : (205, 208)
# pattern = re.compile(r'(?<!not\s)be\b')       #查找前面没有单词not的单词be
# index = 0
# while True:
#      matchResult = pattern.search(exampleString, index)
#  if not matchResult:
#  break
#      print(matchResult.group(0), ':', matchResult.span(0))
#      index = matchResult.end(0)
#
#
# be : (13, 15)
# exampleString[13:20]    #验证一下结果是否正确
# 'be one-'
# pattern = re.compile(r'(\b\w*(?P<f>\w+)(?P=f)\w*\b)') #匹配有连续相同字母的单词
# index = 0
# while True:
#       matchResult = pattern.search(exampleString, index)
#  if not matchResult:
#  break
#       print(matchResult.group(0), ':', matchResult.group(2))
#       index = matchResult.end(0) + 1


unless : s
better : t
better : t
s = 'aabc abcd abbcd abccd abcdd'
p = re.compile(r'(\b\w*(?P<f>\w+)(?P=f)\w*\b)')
p.findall(s)
[('aabc', 'a'), ('abbcd', 'b'), ('abccd', 'c'), ('abcdd', 'd')]

s = "It's a very good good idea"

re.sub(r'(\b\w+) \1', r'\1', s)  #处理连续的重复单词
"It's a very good idea"

re.sub(r'((\w+) )\1', r'\2', s)

"It's a very goodidea"