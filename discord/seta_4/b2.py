O = input()
E = input()

s = len(E)
l = []

for i in range(s):
    l.append(O[i])
    l.append(E[i])

if len(O) - s:
    l.append(O[-1])

print("".join(l))