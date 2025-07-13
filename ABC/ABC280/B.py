n = int(input())
s = list(map(int, input().split()))

a = []
a.append(s[0])
for i in range(n):
    if i+1 >= n: continue
    a.append(s[i+1]-s[i])

print(*a)