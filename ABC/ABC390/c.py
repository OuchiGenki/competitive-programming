H, W = map(int, input().split())
S = [list(input()) for _ in range(H)]

min_r = 10**6
max_r = -1
min_c = 10**6
max_c = -1

for i in range(H):
    for j in range(W):
        if S[i][j] == '#':
            min_r = min(min_r, i)
            min_c = min(min_c, j)
            max_r = max(max_r, i)
            max_c = max(max_c, j)

flag = True
for i in range(min_r, max_r+1):
    for j in range(min_c, max_c+1):
        if S[i][j] == '.':
            flag = False

if flag:
    print("Yes")
else:
    print("No")