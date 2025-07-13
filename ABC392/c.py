N = int(input())
P = list(map(int, input().split()))
Q = list(map(int, input().split()))

qtoi = dict()
for i in range(N):
    qtoi[Q[i]] = i

answer = []
for i in range(1, N+1):
    answer.append(Q[P[qtoi[i]]-1])

print(*answer)
