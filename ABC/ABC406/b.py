N, K = map(int, input().split())
A = list(map(int, input().split()))

score = 1
for i in range(N):
    score *= A[i]
    if len(str(score)) >= K+1:
        score = 1

print(score)