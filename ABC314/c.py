from collections import defaultdict

N, M = map(int, input().split())
S = list(input())
C = list(map(int, input().split()))

pos = defaultdict(list)
for i in range(N):
    pos[C[i]].append(i)

for c in range(1, M+1):
    tmp = S[pos[c][-1]]
    for i in range(len(pos[c])-1, 0, -1):
        S[pos[c][i]] = S[pos[c][i-1]]
    S[pos[c][0]] = tmp

print(''.join(S))