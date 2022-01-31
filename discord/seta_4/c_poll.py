from collections import defaultdict
N = int(input())

d = defaultdict(int)
for _ in range(N):
    s = input()
    d[s] += 1

# print(d.sort())

max_n = max(d.values())
for char in sorted(d):
    if d[char] == max_n:
        print(char)

