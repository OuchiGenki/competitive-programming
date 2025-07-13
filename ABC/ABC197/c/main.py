n = int(input())
a = list(map(int, input().split()))
ans = 1<<60
for i in range(2**n):
    s = []
    for j in range(n):
        if i>>j & 1:
            s.append(1)
        else:
            s.append(0)

    res1 = 0
    res2 = 0
    for j in range(len(s)):
        res1 |= a[j]
        if s[j] == 1:
            res2 ^= res1
            res1 = 0
    res2 ^= res1
    ans = min(ans, res2)

print(ans)