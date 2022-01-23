from collections import deque

N, Q = map(int, input().split())

A = list(map(int, input().split()))

d = deque(A)
for i in range(Q):
    t, x, y = map(int, input().split())
    if t == 1:
        d[x-1], d[y-1] = d[y-1], d[x-1]
    elif t == 2:
        d.rotate()
    else:
        print(d[x-1])


# 正攻法
# shift = 0
# for i in range(Q):
#     t, x, y = map(int, input().split())
#     num_x = (x - shift - 1) % n
#     num_y = (y - shift - 1) % n
#     if t == 1:
#         A[num_x], A[num_y] = A[num_y], A[num_x]
#     elif t == 2:
#         shift += 1
#     else:
#         print(A[num_x])