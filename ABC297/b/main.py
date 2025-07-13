import sys
sys.setrecursionlimit(10**8)
input = sys.stdin.readline

s = input()
b = [i for i, x in enumerate(s) if x=='B']
r = [i for i, x in enumerate(s) if x=='R']
k = s.index('K')

ok = True
if b[0]%2 == b[1]%2:
    ok = False

if ok and r[0] < k < r[1]:
    print("Yes")
else:
    print("No")