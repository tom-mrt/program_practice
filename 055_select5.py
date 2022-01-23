import itertools

N, P, Q = map(int, input().split())
A = list(map(int, input().split()))

count = 0
for v in itertools.combinations(A, 5):
    seki = 1
    for i in range(5):
        if i != 0:
            seki = seki * v[i] % P
        else:
            seki *= v[i]
    if seki == Q:
        count += 1

print(count)

# TLEになってしまう