import numpy as np

def answer(S):
    N = len(S)
    li = []
    for i in range(N):
        for j in range(i+1, N+1):
            li.append(tuple(S[:i] + list(np.roll(S[i:j], -1)) + S[j:]))

    res = list(map(lambda x: chr(x + ord('a')), min(li)))
    return ''.join(res)

T = int(input())
for i in range(T):
    N = int(input())
    S = list(map(lambda x: ord(x)-ord('a'), input()))
    #print(S)
    #print(answer(S))
    if len(S) == 1:
        print(chr(ord('a')+S[0]))
        continue

    left = -1
    for j in range(N-1):
        if S[j] > S[j+1]:
            left = j
            break
    
    if left == -1:
        print(''.join(map(lambda x: chr(ord('a')+x), S)))
        continue
    
    right = left
    while right < N-1 and S[left] >= S[right+1]:
        right += 1
    S = ''.join(map(lambda x: chr(ord('a')+x), S))
    print(S[:left] + S[left+1:right+1] + S[left] + S[right+1:])