def dfs(node, depth):
    visited[node] = True  # 每次搜一个结点就讲节点改成已经遍历
    global max_depth
    max_depth = max(max_depth, depth)  # 更新最大深度
    if node not in tree:  # 判断当前结点是否在tree里，不在就表示是叶子结点
        leave_num[depth] += 1
        return
    for child in tree[node]:  # 如果是父结点就搜索该结点的所有子节点
        if child not in visited:  # 必须判断是否被搜索过，否则会导致无限递归
            dfs(child, depth + 1)


# n为节点数，m为父节点数
n, m = map(int, input().split())
# 用字典存储树能自动对结点排序避免输入乱序，在tree中只保留所有有子结点的结点
tree = {}
for i in range(m):
    node_id, child_num, *children = input().split()  # 输入所有的父节点，子节点个数，子节点id
    tree[node_id] = children  # 将所有父节点保存进树中
# 记录每个深度的叶子节点数量(列表长度应为n+1因为可能出现只有左、右子树的情况)
leave_num = [0 for i in range(n + 1)]
max_depth = 0  # 最大深度决定我们最终搜索到的层数

# dfs算法搜索每层叶子结点个数
visited = {}  # 记录是否遍历过某一结点
dfs('01', 0)
print(" ".join(str(i) for i in leave_num[:max_depth + 1]))
