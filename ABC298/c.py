from sortedcontainers import SortedSet, SortedList
from collections import defaultdict

N = int(input())
Q = int(input())
box = [SortedList() for i in range(N+1)]
card = defaultdict(SortedSet)

for i in range(Q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        i, j = query[1:]
        box[j].add(i)
        card[i].add(j)
    elif query[0] == 2:
        i = query[1]
        print(*box[i])
    else:
        i = query[1]
        print(*card[i])