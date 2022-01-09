N = int(input())

txy = []
for _ in range(N):
    s = list(map(int, input().split()))
    txy.append(s)

# for l in txy:
#     if l[0] % 2 == (l[1]+l[2]) % 2 and l[0] >= l[1]+l[2]:
#         continue
#     else:
#         print("No")
#         break
# else:
#     print("Yes")

for i in range(N):
    if (txy[i][0] + txy[i][1] + txy[i][2]) % 2 == 0 and txy[i][0] >= txy[i][1] + txy[i][2]:
        if i >= 1:
            if abs(txy[i][1] + txy[i][2] - txy[i-1][1] - txy[i-1][2]) <= abs(txy[i][0] - txy[i-1][0]):
                continue
            else:
                print("No")
                break
        continue
    else:
        print("No")
        break
else:
    print("Yes")
