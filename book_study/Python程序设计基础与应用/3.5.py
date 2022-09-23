from random import randrange

# 10个用户，每个用户对3-9个电影进行评分
data = {'user' + str(i) : {'film' + str(randrange(1,15)) : randrange(1,6)
                           for j in range(randrange(3,10))}
                            for i in range(10)}
print(data)

# 当前用户打分
user = {'film' + str(randrange(1,15)) : randrange(1,6) for i in range(5)}
print(user)

f = lambda item: (len(item[1].keys() & user.keys()),
    sum(((item[1].get(film) - user.get(film)) ** 2) for film in user.keys() & item[1].keys()
                  ))
print(f)

# similarUser, films = min(data.items(),key=f)
# print(similarUser,films)

print(user)
for item in data.items():
    # print(item[1])
    print(len(item[1].keys() & user.keys()),
        sum(((item[1].get(film) - user.get(film)) ** 2)
        for film in user.keys() & item[1].keys()),
          item,
          sep='  ')