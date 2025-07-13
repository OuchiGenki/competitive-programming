import sys
sys.setrecursionlimit(10**8)
input = sys.stdin.readline

n = int(input())
s = input()
flag = True
if s[0] == 'F':
    flag = False

ok = True
for i in range(n):
    if flag:
        if s[i] != 'M':
            ok = False
            break
        else:
            flag = False
    else:
        if s[i] != 'F':
            ok = False
            break
        else:
            flag = True

if ok:
    print("Yes")
else:
    print("No")