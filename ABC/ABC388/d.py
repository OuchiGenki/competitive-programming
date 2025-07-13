N = int(input())
A = list(map(int, input().split()))

imos = [0 for i in range(N)]
stones = 0

for i in range(N):
    if i-1 >= 0:
        imos[i] += imos[i-1]
    if i+1 < N:
        imos[i+1] += 1
    if i+A[i]+imos[i]+1 < N:
        imos[i+A[i]+imos[i]+1] -= 1

ans = []
for i in range(N):
    ans.append(max(0, imos[i]+A[i]-(N-i-1)))

print(*ans)