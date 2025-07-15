s = input()
n = int(input())
ans = 0
for i in range(len(s)):
    if s[i] == '1':
        ans += 2**(len(s)-i-1)

if ans > n:
    print(-1)
    exit()

for i in range(len(s)):
    if s[i] == '?' and ans + 2**(len(s)-i-1) <= n:
        ans += 2**(len(s)-i-1)

print(ans)