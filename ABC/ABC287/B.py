n, m = map(int, input().split())
s = [list(input()) for i in range(n)]
t = [list(input()) for i in range(m)]

ans = 0
for i in range(n):
    for j in range(m):
        if s[i][-3:] == t[j]:
            ans += 1
            break

print(ans)