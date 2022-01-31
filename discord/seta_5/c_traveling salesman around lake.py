# https://atcoder.jp/contests/abc160/submissions/me

K, N = map(int, input().split())

A = list(map(int, input().split()))
a0 = A[0]

A_k = [x - A[0] for x in A]

larger = K - A_k[-1]
for i in range(1, N):
    larger = max(larger, A_k[i] - A_k[i-1])

print(K - larger)