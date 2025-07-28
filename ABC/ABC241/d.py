from sortedcontainers import SortedList

q = int(input())
A = SortedList()
for _ in range(q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        x = query[1]
        A.add(x)
    elif query[0] == 2:
        x, k = query[1], query[2]
        idx = A.bisect_right(x)
        if idx - k < 0:
            print(-1)
        else:
            print(A[idx - k])
    elif query[0] == 3:
        x, k = query[1], query[2]
        idx = A.bisect_left(x)
        if idx + k - 1 >= len(A):
            print(-1)
        else:
            print(A[idx + k - 1])