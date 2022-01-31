N, K = map(int, input().split())

A = list(map(int, input().split()))

d = {}
for a in set(A):
    d[a] = 0

for a in A:
    d[a] += 1

count = 0
# TLEの解法
# s = set(A)
# while len(s) > K:
#     min_v = min(d.values()) # o(N)の計算量になるからTLE
#     min_key = min(d, key=d.get)
#     s.remove(min_key)
#     d.pop(min_key)
#     count += min_v

s = len(d) - K
v_list = sorted(d.values())
if s > 0:
    for i in range(s):
        count += v_list[i]

print(count)