S = list(input())
T = ['.' for i in range(len(S))]
n = len(S)
for i in range(n):
    if S[i] == '#':
        T[i] = '#'
flag = True
for i in range(n):
    if T[i] == '#':
        flag = True
        continue
    if flag:
        T[i] = 'o'
        flag = False
print(''.join(T))