# https://atcoder.jp/contests/abc237/tasks/abc237_d

from collections import deque
N = int(input())
S = input()

# A = deque([N])
# s_l = list(S)
# for c in reversed(s_l):
#     N -= 1
#     if c == "L":
#         A.append(N)
#     else:
#         A.appendleft(N)
#
# print(*A)

A = [0]
L = []
R = deque([])

for i in range(N):
    if S[i] == "L":
        R.appendleft(i)
    else:
        L.append(i)

print(*(L + [N] + list(R)))
