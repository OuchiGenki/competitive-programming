import sys, heapq
sys.setrecursionlimit(10**8)

n, m = map(int, input().split())
tws = []

for i in range(m):
    t, w, s = map(int, input().split())
    tws.append([t,w,s])

d = dict()
d[0] = [heapq.heapify([i for i in range(1, n+1)])]

for i in range(m):
    t, w, s = tws[i]