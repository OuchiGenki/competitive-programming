n, k = map(int, input().split())
s = list(input())

cnt = 0
for i in range(n):
    if s[i] == 'o':
        cnt += 1
    if cnt > k:
        s[i] = 'x'

for i in s:
    print(i, end="")
print()