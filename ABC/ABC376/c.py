N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
A.sort(reverse=True)
B.sort(reverse=True)
A_idx = 0
B_idx = 0
x = -1
cnt = 0
for _ in range(N):
    if B_idx == N-1:
        x = A[A_idx]
        cnt += 1
        break
    if A[A_idx] > B[B_idx]:
        x = A[A_idx]
        A_idx += 1
        cnt += 1
    else:
        A_idx += 1
        B_idx += 1

if cnt == 1:
    print(x)
else:
    print(-1)
