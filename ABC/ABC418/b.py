s = input()
n = len(s)
ans = 0
for l in range(n):
    for r in range(l+1, n):
        if (s[l] == s[r] == 't') and r - l + 1 >= 3:
            x = 0
            for i in range(l, r+1):
                if s[i] == 't':
                    x += 1
            ans = max(ans, (x-2) / ((r-l+1) - 2))
print(ans)
