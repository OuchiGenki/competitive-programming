N = int(input())
L, R = [], []
for i in range(N):
    l, r = map(int, input().split())
    L.append(l)
    R.append(r)
L.sort()
R.sort()

cnt = 0
right = 0
for left in range(N):
    while right < N and L[left] > R[right]:
        right += 1
    cnt += right

print(N*(N-1)//2 - cnt)