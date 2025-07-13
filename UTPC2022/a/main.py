import sys
sys.setrecursionlimit(10**8)
input = sys.stdin.readline

t = int(input())
for i in range(t):
    k = input()
    s = set()
    for i in range(len(k)-1):
        s.add(k[i])
    
    if len(s)==1:
        print(k)
    else:
        print(-1)