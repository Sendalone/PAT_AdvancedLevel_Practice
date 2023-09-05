# 输入数据，并保留本来的数据格式
a = [eval(i) for i in input().split()[1:]]
b = [eval(i) for i in input().split()[1:]]
result = {}
# 分别把数据存放入字典
for i in range(0, len(a), 2):
    for j in range(0, len(b), 2):
        if (a[i] + b[j]) in result:
            result[a[i] + b[j]] += a[i + 1] * b[j + 1]
        else:
            result[a[i] + b[j]] = a[i + 1] * b[j + 1]
result = sorted(result.items(), key=lambda d: int(d[0]), reverse=True)
# 输出元素
print(len(result), end="")
for tup in result:
    print(" {} {:.1f}".format(tup[0], tup[1]), end="")
