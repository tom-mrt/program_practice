# https://atcoder.jp/contests/arc061/tasks/arc061_a
# 実装が難しくて解けず。

S = input()
N = len(S)

def dfs(i, f):
    if i==N-1:
        return sum(list(map(int, f.split('+'))))

    #式fの末尾に＋を追加するかしないかで次の数字を追加
    return dfs(i+1, f + S[i+1]) + dfs(i+1, f + '+' + S[i+1])

print(dfs(0, S[0]))


