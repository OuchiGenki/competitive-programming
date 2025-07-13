from itertools import permutations

N, M = map(int, input().split())
S = [input() for i in range(N)]

for v in permutations(range(N)):
    flag = True
    for i in range(1, N):
        diff = 0
        for j in range(M):
            if S[v[i]][j] != S[v[i-1]][j]:
                diff += 1
        if diff != 1:
            flag = False
    if flag:
        print('Yes')
        exit()
print('No')