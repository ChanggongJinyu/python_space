with open('somefile.txt') as f:
    lines = (line.strip() for line in f)
    # 生成器
    print(lines)
    for line in lines:
        print(line)