N = int(input())
A = list(map(int, input().split()))

sorted(A)
d = {}
for i in range(len(A)):
    d[A[i]] = i + 1

for a in reversed(sorted(A)):
    print(d[a])
