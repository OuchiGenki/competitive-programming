N = int(input())
A = list(map(int, input().split()))
W = list(map(int, input().split()))
box = [[] for i in range(N)]
for i in range(N):
    box[A[i]-1].append(W[i])

cost = 0
for i in range(N):
    if len(box[i]) <= 1:
        continue
    box[i].sort()
    for j in range(len(box[i])-1):
        cost += box[i][j]

print(cost)