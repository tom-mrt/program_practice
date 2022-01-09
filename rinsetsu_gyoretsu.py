# 隣接行列の活用
# スプリンクラー(第3回アルゴリズム実技検定E問題）
# https://atcoder.jp/contests/past202005-open/tasks/past202005_e

N, M, Q = map(int, input().split())

# Falseの N * N 二次元配列を作成
graph = []
for i in range(N):
    # 長さ N の False の1次元配列を作る
    row = []
    for j in range(N):
        row.append(False)

    # 長さ N の False の1次元配列を graph に追加する
    graph.append(row)

# M 本の辺を受けとる
for i in range(M):
    u, v = map(int, input().split())

    # 頂点番号はすべて-1する（pythonのリストのindex）
    u -= 1
    v -= 1

    # u, v間には辺があるためTrue
    graph[u][v] = True
    graph[v][u] = True

C = list(map(int, input().split()))

for _ in range(Q):
    query = list(map(int, input().split()))

    # スプリンクラーを起動
    if query[0] == 1:
        x = query[1]
        x -= 1
        print(C[x])

        for i in range(N):
            if graph[x][i]:
                C[i] = C[x]

    # スプリンクラーを起動しない場合
    if query[0] == 2:
        x = query[1]
        y = query[2]
        x -= 1
        print(C[x])
        C[x] = y



