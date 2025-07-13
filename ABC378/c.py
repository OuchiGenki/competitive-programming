N = int(input())
A = list(map(int, input().split()))
d = dict()
answer = []
for i in range(N):
    if A[i] in d:
        answer.append(d[A[i]])
        d[A[i]] = i+1
    else:
        answer.append(-1)
        d[A[i]] = i+1

print(*answer)
