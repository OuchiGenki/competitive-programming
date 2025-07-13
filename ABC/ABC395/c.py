from collections import defaultdict

N = int(input())
A = list(map(int, input().split()))

pos = defaultdict(lambda: -1)
answer = 10**6

for i in range(N):
    if pos[A[i]] == -1:
        pos[A[i]] = i
    else:
        answer = min(answer, i-pos[A[i]]+1)
        pos[A[i]] = i

if answer != 10**6:        
    print(answer)
else:
    print(-1)
