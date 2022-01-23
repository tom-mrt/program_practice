N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

A_c = [0] * 46
for a in A:
    A_c[a % 46] += 1

B_c = [0] * 46
for b in B:
    B_c[b % 46] += 1

C_c = [0] * 46
for c in C:
    C_c[c % 46] += 1

ans = 0
for i in range(46):
    for j in range(46):
        for k in range(46):
            if (i + j + k) % 46 == 0:
                ans += A_c[i] * B_c[j] * C_c[k]

print(ans)