from itertools import permutations

N, M = map(int, input().split())
S = [list(input()) for i in range(N)]
bits = []
for i in range(N):
    tmp = 0
    for j in range(M):
        if S[i][j] == 'o':
            tmp += 2**j
    bits.append(tmp)

ans = float('inf')
for v in permutations(range(N)):
    bit = 0
    cnt = 0
    for idx in v:
        cnt += 1
        bit |= bits[idx]
        if bit == 2**M-1:
            ans = min(ans, cnt)
            break

print(ans)