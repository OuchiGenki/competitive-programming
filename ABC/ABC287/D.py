S = list(input())
T = list(input())
ans = []

diff = 0
for i in range(1, len(T)+1):
    if S[-i] != T[-i] and S[-i] != '?' and T[-i] != '?':
        diff += 1
if diff == 0:
    ans.append('Yes')
else:
    ans.append('No')

for i in range(len(T)-1):
    if S[i] != T[i] and S[i] != '?' and T[i] != '?':
        diff += 1
    if S[-len(T)+i] != T[i] and S[-len(T)+i] != '?' and T[i] != '?':
        diff -= 1
    
    if diff == 0:
        ans.append('Yes')
    else:
        ans.append('No')

diff = 0
for i in range(len(T)):
    if S[i] != T[i] and S[i] != '?' and T[i] != '?':
        diff += 1
if diff == 0:
    ans.append('Yes')
else:
    ans.append('No')

for i in ans:
    print(i)