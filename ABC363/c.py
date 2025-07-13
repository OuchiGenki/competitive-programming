from itertools import permutations

N, K = map(int, input().split())
S = list(input())
u = set()
cnt = 0

for s in permutations(S):
    if s in u:
        continue
    u.add(s)

    flag = False
    for i in range(N-K+1):
        tmp = True
        for j in range(K):
            if s[i+j] != s[i+K-1-j]:
                tmp = False
        if tmp:
            flag = True
            break
    
    if not flag:
        cnt += 1
    
print(cnt)