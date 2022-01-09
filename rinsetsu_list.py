# 隣接リストの活用
# スプリンクラー(第3回アルゴリズム実技検定E問題）
# https://atcoder.jp/contests/past202005-open/tasks/past202005_e

N, M, Q = map(int, input().split())

# 頂点の数だけ、空リスト作成
graph = [[] for _ in range(N)]

# 辺の受け取り
for _ in range(M): # rangeの引数は M 辺の数
    u, v = map(int, input().split())
    u -= 1
    v -= 1

    graph[u].append(v)
    graph[v].append(u)

C = list(map(int, input().split()))

for _ in range(Q):
    query = list(map(int, input().split()))

    if query[0] == 1:
        x = query[1]
        x -= 1
        print(C[x])

        for i in graph[x]: # xに隣接する頂点の探索
            C[i] = C[x]

    if query[0] == 2:
        x = query[1]
        y = query[2]
        x -= 1
        print(C[x])

        C[x] = y