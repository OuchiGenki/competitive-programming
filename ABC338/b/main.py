import sys
sys.setrecursionlimit(10**8)

s = input()

cnt = [0 for i in range(26)]

for c in s:
    cnt[ord(c)-97] += 1

ans = ""
tmp = 0
for i in range(25, -1, -1):
    if cnt[i] >= tmp:
        tmp = cnt[i]
        ans = chr(97+i)

print(ans)