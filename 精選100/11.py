n, m = map(int, input().split())
k = []
s = []
for i in range(m):
    li = list(map(int, input().split()))
    k.append(li[0])
    s.append(li[1:k[i]+1])
p = list(map(int, input().split()))

ans = 0
for i in range(2**n):
    flag = True
    cnt = [0 for i in range(m)]
    for j in range(n):
        if i>>j & 1:
            for u in range(m):
                if j+1 in s[u]:
                    cnt[u] += 1
    for j in range(m):
        if cnt[j]%2 != p[j]:
            flag = False
    if flag:
        ans += 1

print(ans)