N = int(input())
A = list(map(int,input().split()))

ans = 0
for x in range(N+1):
    cnt = 0
    for i in range(N):
        if x <= A[i]:
            cnt += 1
    if cnt >= x:
        ans = x

print(ans)