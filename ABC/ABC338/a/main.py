import sys
sys.setrecursionlimit(10**8)

cnt = 0
s = input()
for c in s:
    if c.isupper():
        cnt += 1

if cnt==1 and s[0].isupper():
    print("Yes")
else:
    print("No")