# https://atcoder.jp/contests/abc236/tasks/abc236_d

# n = int(input())
# a = [[0] * (2 * n) for _ in range(2 * n)]
#
# for i in range(2 * n - 1):
#     l = [int(i) for i in input().split()]
#     for j in range(i + 1, 2 * n):
#         a[i][j] = l[j - i - 1]
#
# used = [False] * (2 * n)
# def rec(i, x):
#     if i == n:
#         return x
#     res = 0
#     for j in range(2 * n):
#         if not used[j]:
#             l = j
#             break
#     used[l] = True
#     for r in range(l + 1, 2 * n):
#         if used[r]:
#             continue
#         used[r] = True
#         res = max(res, rec(i + 1, x ^ a[l][r]))
#         used[r] = False
#     used[l] = False
#     return res
#
# print(rec(0, 0))

n = int(input())
a = [0] * 2*n
for i in range(2*n-1):
    a[i]=list(map(int,input().split()))

ans = 0
def bit_calc(people,value):
    if len(people) == 0:
        global ans
        ans = max(ans,value)
        return
    last = people[-1]
    for i in range(len(people)-1):
        other= people[i]
        bit_calc(people[:i] + people[i+1:-1], value ^ a[other][last-other-1])

bit_calc(list(range(2*n)),0)
print(ans)
