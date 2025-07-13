from collections import defaultdict

N = int(input())
A = list(map(int, input().split()))

cnt = defaultdict(int)
for i in range(N):
    cnt[A[i]] += 1

answer = -1
max_num = 0
for i in range(N):
    if cnt[A[i]] == 1:
        if max_num < A[i]:
            max_num = A[i]
            answer = i+1
            
print(answer)