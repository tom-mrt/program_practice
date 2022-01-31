# https://atcoder.jp/contests/abc158/tasks/abc158_c

A, B = map(int, input().split())

a_l = A * 100 / 8
a_r = (A + 1) * 100 / 8

b_l = B * 100 / 10
b_r = (B + 1) * 100 / 10

if a_l <= b_l < a_r:
    print(int(b_l))
elif b_l <= a_l < b_r:
    if A % 2 == 0:
        print(int(a_l))
    else:
        print(int(a_l) + 1)
else:
    print(-1)