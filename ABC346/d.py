n = int(input())
s = list(map(int,input()))
C = list(map(int, input().split()))
for i in range(n):
    if i % 2:
        s[i] ^= 1
ans = float('inf')
for i in range(2):
    l = [0] * (n + 1)
    r = [0] * (n + 1)
    for i in range(n):
        l[i + 1] += l[i]
        if s[i] == 1:
            l[i + 1] += C[i]
    for i in range(n - 1, -1, -1):
        r[i] += r[i + 1]
        if s[i] == 0:
            r[i] += C[i]
    for i in range(1, n):
        ans = min(ans, l[i] + r[i])
    for i in range(n):
        s[i] ^= 1
print(ans)