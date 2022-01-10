# https://algo-method.com/tasks/536/editorial
from queue import Queue

N, M = map(int, input().split())

G = [[] for _ in range(N)]
deg = [0] * N # 各頂点の出次数を格納。出次数：頂点から出る辺の数

for _ in range(M):
    a, b = map(int, input().split())
    G[a].append(b) # A -> B への辺を張る
    deg[b] += 1

que = Queue()

num = 0 # 出次数0の頂点の数
for v in range(N): # 入次数0の頂点をqueに格納
    if deg[v] == 0:
        que.put(v)
        num += 1

while not que.empty():
    v = que.get()

    for v2 in G[v]: # 入次数0の頂点に隣接する頂点を探索
        deg[v2] -= 1 # 出次数を減らす

        if deg[v2] == 0:
            que.put(v2)
            num += 1

print("Yes" if num == N else "No")