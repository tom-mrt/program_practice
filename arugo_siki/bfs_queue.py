# https://algo-method.com/tasks/418

from queue import Queue

N, M = map(int, input().split())
G = [[] for _ in range(N)]

# 隣接リストの作成　
# 各頂点から1の距離で行ける点のリスト
for _ in range(M):
    a, b = map(int, input().split())
    G[a].append(b)
    G[b].append(a)

dist = [-1] * N # 各点を何手目に探索したか。 -1 で未訪問
que = Queue() # to doリストの作成

# 頂点0を始点にする
que.put(0)
dist[0] = 0

while not que.empty():
    v = que.get() # queueからの頂点の取り出し
    for next_v in G[v]: # v と辺で繋がった点の探索
        if dist[next_v] != -1:
            continue

        dist[next_v] = dist[v] + 1 # 子頂点の探索は親頂点+1手目
        que.put(next_v)



if __name__ == "__main__":
    print(max(dist))

# 入力例1
# 5 4
# 0 1
# 0 2
# 0 3
# 0 4

# 出力
# 1

# 入力例2
# 6 7
# 0 1
# 0 5
# 1 3
# 1 5
# 2 3
# 3 4
# 4 5

# 出力
# 3