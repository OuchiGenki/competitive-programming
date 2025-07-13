import sys, copy
sys.setrecursionlimit(10**8)

p = [[list(input()) for i in range(4)] for j in range(3)]

def rotate(a):
    b = copy.deepcopy(a)
    for i in range(4):
        for j in range(4):
            a[j][3-i] = b[i][j]

def can_place(grid, cnt, di, dj):

    for i in range(4):
        for j in range(4):
            if p[cnt][i][j] == "#":
                r = i+di
                c = j+dj
                if r<0 or r>=4 or c<0 or 4<=c:
                    return False
                if grid[r][c] == 1:
                    return False
                grid[r][c] = 1
    return True

def dfs(cnt, grid):
    if cnt == 3:
        ok = 1
        for i in range(4):
            for j in range(4):
                ok &= grid[i][j]
        if (ok):
            print("Yes")
            exit()
        else:
            return

    for di in range(-3, 4):
        for dj in range(-3, 4):
            now_grid = copy.deepcopy(grid)
            if can_place(now_grid, cnt, di, dj):
                dfs(cnt+1, now_grid)


for i in range(4):
    for j in range(4):
        dfs(0, [[0 for i in range(4)]for j in range(4)])
        rotate(p[1])
    rotate(p[2])

print("No")