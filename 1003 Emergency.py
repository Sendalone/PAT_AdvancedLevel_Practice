# 创建点类
class Vertex:
    def __init__(self, key, num):  # key,num分布记录点的名称和包含救援队数量
        self.key = key
        self.num = num
        self.connect = {}

    def connect_vertex(self, other, cost):  # 将两个点连接
        self.connect[other] = cost

    def cost(self, to):  # 返回该点到其他点的距离
        if to in self.connect.keys():
            return self.connect[to]


# 创建图类
class Graph:
    def __init__(self):  # ver_list储存所有点，num记录点的数量
        self.ver_list = {}
        self.vertex_num = 0

    def add_vertex(self, key, num):  # 添加点
        self.vertex_num += 1
        new_vertex = Vertex(key, num)
        self.ver_list[key] = new_vertex
        return new_vertex

    def exist_vertex(self, key):  # 判断点是否存在
        if key in self.ver_list:
            return None
        else:
            return True

    def add_edge(self, fv, tv, cost, numf, numv):  # 给两点加边
        # 若点不存在则创建点
        if self.exist_vertex(fv):
            self.add_vertex(fv, numf)
        if self.exist_vertex(tv):
            self.add_vertex(tv, numv)
        # 分别对起始点和终点添加一个边来制作无向图
        self.ver_list[fv].connect_vertex(tv, cost)
        self.ver_list[tv].connect_vertex(fv, cost)

    def neighbor(self, v):
        if v in self.ver_list:
            return self.ver_list[v].connect.keys()

    def move_cost(self, fv, tv):  # 返回从起始点到终点所花费的距离
        return self.ver_list[fv].cost(tv)

    def get_vertex(self, key):
        return self.ver_list[key]

    def __iter__(self):
        return iter(self.ver_list.values())


# 输入数据
graph = Graph()  # 建图
N, E, C1, C2 = map(int, input().split())  # 城市数量，边数，所在地，目的地
rescue_num = {}
num_inp = list(map(int, input().split()))
for i in range(N):
    rescue_num[i] = rescue_num.get(i, num_inp[i])  # 救援队数量

for i in range(E):
    f, t, c = map(int, input().split())  # 两个点和距离
    graph.add_edge(f, t, c, rescue_num[f], rescue_num[t])
# Dijkstra 算法求最短路
open_list = {C1: 0}  # 存放已经访问的从该节点到起点有路径的结点
close_list = {}  # 存放那些已经找到最优路径的结点
parents = {C1: None}  # 存放结点的父子关系
ans = [0 for n in range(N)]
ans[C1] = rescue_num[C1]  # 记录救援队数量
min_dis_num = [0 for n in range(N)]
min_dis_num[C1] = 1  # 记录最短路径数量
while True:
    min_vertex = min(open_list, key=lambda x: open_list[x])  # 找到距离最短的节点
    min_edge = open_list[min_vertex]  # 找到最短的距离
    open_list.pop(min_vertex)
    close_list[min_vertex] = min_edge  # 添加到close_list里面
    min_cost = None  # 记录最短路长度

    # 当找到终点时即找到最短路径
    if min_vertex == C2:
        print(min_dis_num[C2], ans[C2], sep=" ", end="")
        break

    # 遍历当前节点的邻接节点
    for vertex in graph.neighbor(min_vertex):
        if vertex not in close_list.keys():  # 邻接节点不在 closed_list 中
            if vertex in open_list.keys():  # 如果节点在 open_list 中
                if graph.move_cost(vertex, min_vertex) + min_edge < open_list[vertex]:
                    # 更新节点的值
                    open_list[vertex] = min_edge + graph.move_cost(vertex, min_vertex)
                    # 更新继承关系
                    parents[vertex] = min_vertex
                    # 更新最大救援队数量
                    ans[vertex] = ans[min_vertex] + rescue_num[vertex]
                    # 更新当前路径数量
                    min_dis_num[vertex] = min_dis_num[min_vertex]
                # 如果先到min_vertex，再从min_vertex到vertex的距离与已知直接到vertex的距离相同
                elif graph.move_cost(vertex, min_vertex) + min_edge == open_list[vertex]:
                    # 更新节点的值
                    open_list[vertex] = min_edge + graph.move_cost(vertex, min_vertex)
                    # 更新继承关系
                    parents[vertex] = min_vertex
                    # 更新当前路径数量,因为多了一种走法所以要加上当前的这种走法
                    min_dis_num[vertex] += min_dis_num[min_vertex]
                    # 如果最大救援队数量小于实际最大救援队数量
                    if ans[vertex] < ans[min_vertex] + rescue_num[vertex]:
                        ans[vertex] = ans[min_vertex] + rescue_num[vertex]
            else:  # 如果节点不在 open_list 中
                # 计算节点的值，并加入 open_list 中
                open_list[vertex] = min_edge + graph.move_cost(vertex, min_vertex)
                # 更新继承关系
                parents[vertex] = min_vertex
                # 更新最大救援队数量
                ans[vertex] = ans[min_vertex] + rescue_num[vertex]
                # 更新当前路径数量
                min_dis_num[vertex] = min_dis_num[min_vertex]
