S = input()
T = input()
ans = 'Yes'
for i in range(1, len(S)):
    if S[i].isupper():
        if S[i-1] not in T:
            ans = 'No'
print(ans)