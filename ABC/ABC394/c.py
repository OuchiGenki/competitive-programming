S = list(input())
S.reverse()
for i in range(len(S)-1):
    if S[i:i+2] == ['A', 'W']:
        S[i:i+2] = ['C', 'A']
S.reverse()
print(''.join(S))
