buy_list = []
ans = 1
for i in range(3):
    W, T, L = map(float, input().split())
    dic = {"W": W, "T": T, "L": L}
    ans *= max(W, T, L)
    buy_list.append(max(dic.items(), key=lambda x: x[1]))
ans = (ans * 0.65 - 1) * 2
print(" ".join(x[0] for x in buy_list), f"{ans:.2f}", end="\n")
