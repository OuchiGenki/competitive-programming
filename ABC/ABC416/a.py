n, l, r = map(int, input().split())
S = input()
flag = True
for i in range(l-1, r):
    if S[i] != 'o':
        flag = False
if flag:
    print('Yes')
else:
    print('No')