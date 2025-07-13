import bisect

N = int(input())
A = list(map(int, input().split()))

answer = 0
for i in range(N):
    answer += N - bisect.bisect_left(A, A[i]*2)

print(answer)