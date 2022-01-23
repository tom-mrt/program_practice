#https://atcoder.jp/contests/abc003/submissions/28033006

N, K = map(int, input().split())

R = list(map(int, input().split()))

R.sort()

rate = 0
for n in R[N - K:]:
    rate = (rate + n) / 2

print(rate)
