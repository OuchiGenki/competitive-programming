S = input()
T = input()
X = []

while S != T:
    option = []
    for i in range(len(S)):
        if S[i] != T[i]:
            option.append(S[:i] + T[i] + S[i+1:])
    
    if len(option) == 0:
        break

    option.sort()
    X.append(option[0])
    S = option[0]

print(len(X))
for i in X:
    print(i)
