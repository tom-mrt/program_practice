a, b = map(int, input().split())

def gcd(a, b):
    while b != 0:
        a, b = b, a%b

    return a

# def gcd(a, b):
#     while a != b:
#         if a > b:
#             a, b = b, a-b
#         else:
#             a, b = b, b-a
#     return a

ans = a * b // gcd(a, b)

if ans > 1e18:
    print("Large")
else:
    print(int(ans))