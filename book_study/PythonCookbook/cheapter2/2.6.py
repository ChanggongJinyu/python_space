import re


def matchcase(word):
    print(word)
    def replace(m):
        print("m: ",m)
        text = m.group()
        print('text: ',text)
        if text.isupper():
            return word.upper()
        elif text.islower():
            return word.lower()
        elif text[0].isupper():
            return word.capitalize()
        else:
            return word
    print('11111111111')
    return replace

import re
text = 'UPPER PYTHON, lower python, Mixed Python'
print(re.sub('python',matchcase('snake'),text,flags=re.IGNORECASE))