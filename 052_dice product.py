N = int(input())

A = []
for _ in range(N):
    A.append(sum(list(map(int, input().split()))))

ans = 1
for i in A:
    ans *= i

print(ans % (10**9 + 7))

