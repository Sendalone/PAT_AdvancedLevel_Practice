N = int(input())
num_list = [int(i) for i in input().split()]

start = 0  # 记录子序列的起始位置
end = 0  # 记录子序列的终止位
temp_max_ans = num_list[0]  # 记录当前位置前一位为止加和的子序列的和
temp_start = 0  # 记录每次重置子序列起始位置
ans = temp_max_ans  # 记录目前得到的最大子序列的和

for i in range(1, N):
    if temp_max_ans < 0:  # 判断当前位置前一位为止加和的子序列的和是否小于0，如果已经小于0则应从当前位置重新开始加和
        temp_max_ans = 0
        temp_start = i
    temp_max_ans += num_list[i]
    if temp_max_ans > ans:  # 如果目前加和的子序列大于目前得到的最大子序列
        ans = temp_max_ans  # 更新最大值
        start = temp_start  # 则将开始位置改为前面储存的start的位置
        end = i + 1  # 并把end的位置放在当前位置后一位
if ans < 0:  # 如果最大子序列的和为负数，则意味着最小序列和必定是负数，根据题目意思应该输出0
    print(0, num_list[0], num_list[N - 1], end="")
else:
    print(ans, num_list[start], num_list[end - 1], end="")
