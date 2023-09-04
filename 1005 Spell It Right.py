words = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
num_list = [i for i in input()]  # 输入数字
ans_list = [i for i in str(sum(int(n) for n in num_list))]  # 求和
print(" ".join(words[int(i)] for i in ans_list))
