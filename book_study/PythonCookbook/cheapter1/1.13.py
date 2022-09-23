# 通过公共键对字典列表排序

rows = [
    {'fname': 'Brian', 'lname': 'Jones', 'uid': 1003},
    {'fname': 'David', 'lname': 'Beazley', 'uid': 1002},
    {'fname': 'John', 'lname': 'Cleese', 'uid': 1001},
    {'fname': 'Big', 'lname': 'Jones', 'uid': 1004}
]

from operator import itemgetter
rows_by_fname = sorted(rows, key=itemgetter('fname'))
# 比lambda速度更快
print(rows_by_fname)

rows_by_lfname = sorted(rows, key=itemgetter('fname', 'lname'))
print(rows_by_lfname)

print(sorted(rows,key=lambda x: x['fname']))