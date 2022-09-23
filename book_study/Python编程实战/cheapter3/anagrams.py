# 寻找易位词


import load_dictionary

word_list = load_dictionary.load(r"D:\code\note\python\Python编程实战\12dicts-6.0.2\International\2of4brif.txt")
print(len(word_list))
print(word_list[0])
angram_list = []

name = 'Foster'
print('Input name = {}'.format(name))
name = name.lower()
print('Using name = {}'.format(name))

name_sorted = sorted(name)
print(name_sorted)
for word in word_list:
    if word != name:
        if (sorted(word)) == name_sorted:
            angram_list.append(word)

print()
if (len(angram_list)) == 0:
    print('You need a larger dictionary or a new name!')
else:
    print('Angramw =',*angram_list,sep='\n')

# 60388
# aah
# Input name = Foster
# Using name = foster
# ['e', 'f', 'o', 'r', 's', 't']
#
# Angramw =
# forest
# fortes
# softer
