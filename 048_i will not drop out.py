N, K = map(int, input().split())

score = []
for k in range(N):
    A, B = map(int, input().split())
    score.append(B)
    score.append(A-B)

score.sort(reverse=True)

ans = 0

for k in range(K):
    ans += score[k]

print(ans)