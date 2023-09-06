def transform_decimal(num, radix, times=0):  # 把36进制以内的数转化为十进制
    ans = 0
    for n in reversed(num):  # 逆序遍历
        ans += int(n, 36) * (radix ** times)  # 对于每一位的数字先转换成36进制第数字再乘以radix及次方
        times += 1
    return ans


def find(n, target):
    lower = max([int(x, 36) for x in target]) + 1  # 最小进制为数位上的最大数+1
    upper = max(n, lower)  # 最大进制为n，但如果n为0或1的话不满足查找条件，所以需要比较和lower的大小
    while upper >= lower:  # 二分查找
        mid = (upper + lower) // 2
        temp = transform_decimal(target, mid)
        if temp == n:
            return mid
        else:
            if temp > n:
                upper = mid - 1  # 过大左移
            else:
                lower = mid + 1  # 过小右移
    return "Impossible"


n1, n2, tag, r = input().split()
if tag == "1":
    trans = transform_decimal(n1, int(r))  # 将已知进制的数转化为十进制
    print(find(trans, n2))
if tag == "2":
    trans = transform_decimal(n2, int(r))  # 将已知进制的数转化为十进制
    print(find(trans, n1))
