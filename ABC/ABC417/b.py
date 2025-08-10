from sortedcontainers import SortedList
n, m = map(int, input().split())
A = SortedList(map(int, input().split()))
B = list(map(int, input().split()))
for i in range(m):
    A.discard(B[i])
print(*A)