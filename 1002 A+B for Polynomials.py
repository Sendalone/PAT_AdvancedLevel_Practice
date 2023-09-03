# 输入数据，并保留本来的数据格式
a = [eval(i) for i in input().split()[1:]]
b = [eval(i) for i in input().split()[1:]]
result = {}
# 分别把数据存放入字典
for i in range(0, len(a), 2):
    result[a[i]] = result.get(a[i], 0) + a[i + 1]

for i in range(0, len(b), 2):
    result[b[i]] = result.get(b[i], 0) + b[i + 1]

# 删除系数为0的项
for i in list(result.keys()):
    if result[i] == 0:
        del result[i]

result = sorted(result.items(), key=lambda d: int(d[0]), reverse=True)

# 输出元素
print(len(result), end="")
for tup in result:
    print(" {} {:.1f}".format(tup[0], tup[1]), end="")
