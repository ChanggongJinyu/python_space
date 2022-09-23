import re

text = 'Computer says "no." Phone says "yes."'

# 贪心策略
str_pat = re.compile(r'\"(.*)\"')
print(str_pat.findall(text))
# ['no." Phone says "yes.']

# 懒惰策略
str_pat = re.compile(r'\"(.*?)\"')
print(str_pat.findall(text))
# ['no.', 'yes.']