n = int(input())
s = input()
before = s[0]
ans = 0
for i in range(1, n):
    if s[i] != before:
        ans += 1
        before = s[i]
print(ans+1)