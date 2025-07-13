H, W, N = map(int, input().split())
T = input()
T = T[::-1]
S = [input() for i in range(H)]

def f(y, x):
    global T
    flag = True

    for i in range(N):
        if T[i] == 'L':
            x += 1
        if T[i] == 'R':
            x -= 1
        if T[i] == 'U':
            y += 1
        if T[i] == 'D':
            y -= 1

        if y < 0 or y >= H or x < 0 or x >= W:
            flag = False
            break
        if S[y][x] == '#':
            flag = False
    
    return flag

ans = 0
for i in range(H):
    for j in range(W):
        if S[i][j] == '#':
            continue
        if f(i, j):
            ans += 1

print(ans)