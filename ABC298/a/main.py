import sys
sys.setrecursionlimit(10**8)

n = int(input())
s = input()

ok = True
cnt = 0
for i in s:
    if i == 'x':
        ok = False
    if i == 'o':
        cnt += 1

if ok and cnt > 0:
    print("Yes")
else:
    print("No")