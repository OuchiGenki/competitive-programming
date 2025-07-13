import sys
sys.setrecursionlimit(10**8)
input = sys.stdin.readline

def copy():
    for i in range(n):
        for j in range(n):
            a[i][j] = c[i][j]

def check():
    flag = True
    for i in range(n):
        for j in range(n):
            if a[i][j]==1 and b[i][j]==0:
                flag = False
    return flag

n = int(input())
a = [list(map(int, input().split())) for j in range(n)]
b = [list(map(int, input().split())) for j in range(n)]

c = [[0 for i in range(n)] for j in range(n)]

for k in range(4):
    for i in range(n):
        for j in range(n):
            c[i][j] = a[n-j-1][i]
    copy()
    if check():
        print("Yes")
        exit()

print("No")