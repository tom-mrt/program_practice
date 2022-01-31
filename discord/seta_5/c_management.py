# https://atcoder.jp/contests/abc163/tasks/abc163_c

N = int(input())

A = list(map(int, input().split()))

l = [[] for _ in range(N)]

for n in A:
    l[n-1].append(1)

for li in l:
    print(sum(li))