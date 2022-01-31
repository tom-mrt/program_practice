N, M = map(int, input().split())

def f(x):
    if x == 0:
        return  1
    if x == 1:
        return 1
    return f(x-1) + f(x-2)

ans = 0
A = []
for i in range(M):
    a = int(input())
    A.append(a)

for i in range(M + 1):



print(ans)

