N, M = map(int, input().split())
A = list(map(int, input().split()))
s = set()
for i in range(N):
    s.add(A[i])
    if len(s) == M:
        print(N-i)
        exit()
print(0)