from collections import defaultdict
from sortedcontainers import SortedList

base = 0
lst = SortedList()

q = int(input())
for _ in range(q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        x = query[1]
        lst.add(x - base)
    elif query[0] == 2:
        x = query[1]
        base += x
    elif query[0] == 3:
        if lst:
            print(lst[0]+base)
            lst.remove(lst[0])
        else:
            print(base)
