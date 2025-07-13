import sys
sys.setrecursionlimit(10**8)

def f(y, x, step, dir):
    global N

    if G[y][x] == 'T':
        return
    G[y][x] = step

    ny, nx = y+dir[0], x+dir[1]
    if dir==(0, 1) and (nx == N or G[ny][nx] != -1):
        nx -= 1
        ny += 1
        dir = (1, 0)
    if dir==(1, 0) and (ny == N or G[ny][nx] != -1):
        ny -= 1
        nx -= 1
        dir = (0, -1)
    if dir==(0, -1) and (nx == -1 or G[ny][nx] != -1):
        nx += 1
        ny -= 1
        dir = (-1, 0)
    if dir==(-1, 0) and (ny == -1 or G[ny][nx] != -1):
        ny += 1
        nx += 1
        dir = (0, 1)

    f(ny, nx, step+1, dir)

N = int(input())
G = [[-1 for i in range(N)] for j in range(N)]
G[N//2][N//2] = 'T'

f(0, 0, 1, (0, 1))

for row in G:
    print(*row)