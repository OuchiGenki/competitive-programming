N, A, B = map(int, input().split())
S = input()
ans = float('inf')
for i in range(N):
    cost = A * i
    for j in range(N//2):
        if S[(i+j)%N] != S[(i+N-j-1)%N]:
            cost += B
    ans = min(ans, cost)
print(ans)