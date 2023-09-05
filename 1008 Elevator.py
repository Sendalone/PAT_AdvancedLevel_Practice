floor_list = list(map(int, input().split()))
floor_list.pop(0)
floor_now = 0
ans = 0
for i in floor_list:
    if i > floor_now:
        ans += 6 * (i - floor_now) + 5
    else:
        ans += 4 * (floor_now - i) + 5
    floor_now = i
print(ans)
