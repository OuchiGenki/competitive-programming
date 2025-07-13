s = list(input())
s.reverse()
base = 26
ans = 0
for i in range(len(s)):
    tmp = ord(s[i])-64
    ans += base**i*tmp
print(ans)