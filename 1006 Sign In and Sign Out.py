import datetime

N = int(input())
number_list = []  # 创建一个空列表number_list，用于存储输入的时间序列数据
ans = []  # 创建一个空列表ans，用于存储结果

for i in range(N):
    number_list.append((input().split()))  # 将输入的数据以空格为分隔符分割，并存储到number_list中

for number in number_list:  # 将字符串时间转换为datetime对象方便后面排序寻找最早最晚时间
    number[1] = datetime.datetime.strptime(number[1], '%H:%M:%S')
    number[2] = datetime.datetime.strptime(number[2], '%H:%M:%S')

number_list.sort(key=lambda x: x[1])  # 找到最早时间
ans.append(number_list[0][0])  # 把最早的时间添加到ans中
number_list.sort(key=lambda x: x[2], reverse=True)  # 找到最晚时间
ans.append(number_list[0][0])  # 把最晚的时间添加到ans中
print(" ".join(i for i in ans))
