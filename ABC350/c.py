N = int(input())
A = list(map(int, input().split()))
pos = {A[i]: i for i in range(N)}

res = []
for i in range(N):
    if A[i] == i+1:
        continue
    j = pos[i+1]
    res.append((i+1, j+1))
    pos[A[i]] = j
    pos[A[j]] = i
    A[i], A[j] = A[j], A[i]

print(len(res))
for row in res:
    i, j = row
    if i > j:
        i, j = j, i
    print(i, j)