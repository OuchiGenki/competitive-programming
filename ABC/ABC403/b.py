T = input()
U = input()

for i in range(len(T)):
    flag = True
    for j in range(len(U)):
        if i+j >= len(T):
            flag = False
            continue
        if T[i+j] != '?' and T[i+j] != U[j]:
            flag = False
    if flag:
        break

if flag:
    print('Yes')
else:
    print('No')