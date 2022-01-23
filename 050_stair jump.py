import sys
sys.setrecursionlimit(10 ** 6)

N, L = map(int, input().split())

log = [0] * (N + 1)
log[0] = 1

done = [False] * (N + 1)
done[0] = True

def func(n, l):
    if done[n]:
        return log[n]

    if 1 <= n < l:
        log[n] = func(n-1, l)
    else:
        log[n] = func(n-1, l) + func(n-l, l)
    done[n] = True
    return log[n]

print(func(N, L) % (1000000007))

# dpパターン
# dp = [0 for _ in range(N + 1)]
# dp[0] = 1
#
# for i in range(N):
#     if i + 1 < L:
#         dp[i + 1] = dp[i]
#     else:
#         dp[i + 1] = dp[i] + dp[i - L + 1]
#
# print(dp[N] % 1000000007)
