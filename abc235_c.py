# C_the Kth time query

n,q = map(int,input().split())
a = list(map(int,input().split()))
c = {}
for i in range(n):
  if a[i] not in c:
    c[a[i]] = []
  c[a[i]].append(i+1)
for i in range(q):
  x,k = map(int,input().split())
  if x in c:
    if len(c[x]) >= k:
      print(c[x][k-1])
    else:
      print(-1)
  else:
    print(-1)
