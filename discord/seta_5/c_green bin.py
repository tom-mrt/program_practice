from collections import Counter

# D = []
# for _ in range(N):
#     d = {}
#     s = input()
#     for c in set(s):
#         d[c] = 0
#     for c in s:
#         d[c] += 1
#     D.append(d)
#
# count = 0
# for i in range(len(D)):
#     for j in range(i+1, len(D)):
#         if D[i] == D[j]:
#             count += 1

# print(count)

from collections import defaultdict

n = int(input())
D = defaultdict(int)
for _ in range(n):
    s = list(input())
    s.sort()
    s = "".join(s)
    D[s] += 1

ans = 0
for d in D.values():
    ans += d * (d-1) // 2
print(ans)


