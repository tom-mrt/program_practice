# https://atcoder.jp/contests/abc205/tasks/abc205_d

N, Q = map(int, input().split())
A = list(map(int, input().split()))

# i = 1
# count_l = []
# count = 0 # iより小さい数値の個数
#
# ans = 0
# ans_l = []
# K = []
# for _ in range(Q):
#     k = int(input())
#     K.append(k)
#
# max_k = max(K)
#
# # iより小さい数値の個数を数え、count_lに格納
# # countの上限はKの最大値
# while count < max_k:
#
#     # A内の数値のときには、countを増やさない
#     if i - 1 in A:
#         count_l.append(count - 1)
#     else:
#         count_l.append(count)
#         count += 1
#     i += 1

# k番目に小さい数は、自分より小さい値の個数がk-1の数値の中でインデックスが最大の数
# 上述のインデックス最大の数は、count_lの先頭から、自身より小さい値の個数がk-1までの数値の個数の合計で表現できる
# for num in range(max_k):
#     ans += count_l.count(num)
#     ans_l.append(ans)
#
# for k in K:
#     print(count_l.index(k-1) + count_l.count(k-1))
#
# print(count_l)

count_A = []
for i in range(N):
    count_A.append(A[i] - (i + 1))

for _ in range(Q):
    k = int(input())
    if count_A[-1] < k:
        print(A[-1] + k - count_A[-1])
    else:
        left = 0
        right = len(count_A)
        while abs(left - right) > 0:
            mid = (left + right) // 2
            if count_A[mid] > k - 1:
                right = mid
            else:
                left = mid + 1
        print(A[left] - 1 - (count_A[left] - k))




