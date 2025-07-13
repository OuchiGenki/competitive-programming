import sys
from heapq import *
sys.setrecursionlimit(10**8)
input = sys.stdin.readline

n = int(input())
q = int(input())
hq = [[] for i in range(n+1)]
hq2 = [set() for i in range(2*10**5+1)]

for i in range(q):
    li = list(map(int, input().split()))
    x = li[0]

    if x == 1:
        i = li[1]
        j = li[2]
        hq[j].append(i)
        hq2[i].add(j)
    
    elif x == 2:
        i = li[1]
        hq[i].sort()
        print(*hq[i])
    
    else:
        i = li[1]
        a = sorted(list(hq2[i]))
        print(*a)