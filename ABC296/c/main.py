import sys
sys.setrecursionlimit(10**8)
input = sys.stdin.readline

n, x = map(int, input().split())
a = list(map(int, input().split()))

s = set()
for i in a:
    if i in s:
        print("Yes")
        exit()
    s.add(i+x)
    s.add(i-x)
for i in a:
    if i in s:
        print("Yes")
        exit()
    s.add(i+x)
    s.add(i-x)
print("No")