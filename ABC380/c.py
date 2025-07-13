N, K = map(int, input().split())
S = input()

A = [(-1,-1)]
for i in range(N):
    if S[i] == '0':
        if A[-1][0] == '0':
            A[-1][1] += 1
        else:
            A.append(['0', 1])
    else:
        if A[-1][0] == '1':
            A[-1][1] += 1
        else:
            A.append(['1', 1])

if S[0] == '0':
    k_idx = 2*K
else:
    k_idx = 2*K-1
A[k_idx-2][1] += A[k_idx][1]
A[k_idx][1] = 0

answer = []
for c, cnt in A:
    if c == -1 and cnt == -1:
        continue
    while cnt > 0:
        answer.append(c)
        cnt -= 1

print(''.join(answer))
