S = input()
N = len(S)
T = input()
cnt = [0, 0, 0]
for i in range(N):
    if S[i].upper() == T[0] and cnt[0] == 0:
        cnt[0] += 1
    elif S[i].upper() == T[1] and cnt[0] > 0 and cnt[1] == 0:
        cnt[1] += 1
    elif S[i].upper() == T[2] and cnt[1] > 0:
        cnt[2] += 1

if T[2] != 'X' and cnt[2] > 0:
    print('Yes')
elif T[2] == 'X' and cnt[1] > 0:
    print('Yes')
else:
    print('No')
