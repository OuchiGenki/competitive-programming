N, M = map(int, input().split())
A = []
for _ in range(M):
    li = list(map(int, input().split()))
    A.append(li[1:])
B = list(map(int, input().split()))

pos = dict()
for i in range(N):
    pos[B[i]] = i

answer = [0] * N
for i in range(M):
    max_value = 0
    for j in range(len(A[i])):
        ingredient = A[i][j]
        max_value = max(max_value, pos[ingredient])
    answer[max_value] += 1

for i in range(N-1):
    answer[i+1] += answer[i]

for i in answer:
    print(i)