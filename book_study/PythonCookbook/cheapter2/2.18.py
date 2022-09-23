# 文本分词

text = 'foo = 23 + 42 * 10'

import re
NAME = r'(?P<Name>[a-zA-Z_][a-zA-Z_0-9]*)'
NUM = r'(?P<NUM>\d+)'
PLUS = r'(?P<PLUS>\+)'
TIMES = r'(?P<TIMES>\*)'
EQ = r'(?P<EQ>=)'
WS = r'(?P<WS>\s+)'

master_pat = re.compile('|'.join([NAME,NUM,PLUS,TIMES,EQ,WS]))
print(master_pat)

from collections import namedtuple
Token = namedtuple('Token',['type','value'])

def generate(pat, text):
    scanner = pat.scanner(text)
    for m in iter(scanner.match, None):
        yield Token(m.lastgroup,m.group())

for tok in generate(master_pat,'foo = 42'):
    print(tok)

print('=================================')

tokens = (tok for tok in generate(master_pat,text) if tok.type != 'WS')
for tok in tokens:
    print(tok)