# import bisect
#
# N = int(input())
#
# A = list(map(int, input().split()))
# B = list(map(int, input().split()))
# C = list(map(int, input().split()))
# # A.sort()
# B.sort()
# C.sort()
#
# ans = 0
# for a in A:
#     left = -1
#     right = N
#     while abs(left - right) > 1:
#         mid = (left + right) // 2
#         if B[mid] > a:
#             right = mid
#         else:
#             left = mid + 1
#     if right == N:
#         continue
#     for b in B[right:]:
#         left = -1
#         right = N
#         while abs(left - right) > 1:
#             mid = (left + right) // 2
#             if C[mid] > b:
#                 right = mid
#             else:
#                 left = mid + 1
#        index = min(left, right)
#         ans += len(C[right:])
#
# print(ans)


# C - Snuke Festival

# def countUnder(n):
#   ok = -1
#   ng = N
#
#   while ng - ok > 1:
#     mid = (ok + ng) // 2
#
#     if l1[mid] < n:
#       ok = mid
#     else:
#       ng = mid
#
#   return ok + 1
#
# def countOver(n):
#   ok = N
#   ng = -1
#
#   while ok - ng > 1:
#     mid = (ok + ng) // 2
#
#     if l3[mid] > n:
#       ok = mid
#     else:
#       ng = mid
#
#   return N - (ng + 1)
#
#
# N = int(input())

# l1 = [int(x) for x in input().split()]
# l2 = [int(x) for x in input().split()]
# l3 = [int(x) for x in input().split()]
#
# l1.sort()
# l3.sort()
#
# result = 0
# for each in l2:
#   un = countUnder(each)
#   ov = countOver(each)
#
#   result += (un * ov)
#
# print(result)


# N = int(input())
# ABC = [list(map(int, input().split())) for _ in range(3)]
# for i in range(3):
#     ABC[i].sort()
#
# dp = [[1] * N] + [[0] * N for _ in range(2)]
# for i in range(2):
#     tmp = 0
#     k = 0
#     for j in range(N):
#         while k < N and ABC[i + 1][j] > ABC[i][k]:
#             tmp += dp[i][k]
#             k += 1
#         dp[i + 1][j] = tmp
# print(sum(dp[2]))

n = int(input())
vals = [sorted([int(i) for i in input().split()]) for _ in range(3)]

dp = [[0 for _ in range(n)] for _ in range(3)]
for i in range(n):
    dp[0][i] += 1
"""
dp[i][j] j????????????????????????????????????????????????i?????????????????????????????????
?????????
 dp[0][j] = 1 (0<=j<n) ??????????????????????????????=1??????
 dp[i][j] = 0 (1<=i<=2, 0<=j<n)
"""


def naive():
    # O(N^2)??????
    for i in range(2):
        # i=0 ?????????i=1 ?????????i=2 ??????
        # i=0??????????????????????????? i=1???????????????????????????
        for j in range(n):
            for k in range(n):
                # ???????????????j?????????????????????????????????k???????????????????????????
                if vals[i + 1][j] > vals[i][k]:
                    dp[i + 1][j] += dp[i][k]
    return dp


def solve():
    for i in range(2):
        # i=0 ?????????i=1 ?????????i=2 ??????
        # i=0??????????????????????????? i=1???????????????????????????
        left = 0
        right = 0
        while left < n and right < n:
            # ?????????
            # left : ???????????????left??????????????????
            # right : ????????????right??????????????????
            if vals[i + 1][right] > vals[i][left]:
                dp[i + 1][right] += dp[i][left]
                left += 1
            else:
                right += 1
        for j in range(n - 1):
            # ?????????
            dp[i + 1][j + 1] += dp[i + 1][j]
    return dp


dp = solve()
ans = 0
for i in range(n):
    ans += dp[2][i]
print(ans)
