n = int(input())
s = [[i, input()] for i in range(n)]

s.sort(key=lambda x:x[1])

ans = [0 for i in range(n)]
for i in range(n):
    res1 = res2 = 0
    skip1 = skip2 = False

    for j, k in enumerate(s[i][1]):
        if i > 0 and j < min(len(s[i][1]), len(s[i-1][1])) and not skip1:
            if s[i-1][1][j] == k:
                res1 += 1
            else:
                skip1 = True
        
        if i < n-1 and j < min(len(s[i][1]), len(s[i+1][1])) and not skip2:
            if s[i+1][1][j] == k:
                res2 += 1
            else:
                skip2 = True

    ans[s[i][0]] = max(res1, res2)

for i in ans:
    print(i)