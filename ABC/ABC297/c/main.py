import sys
sys.setrecursionlimit(10**8)

h, w = map(int, input().split())
s = [list(input()) for i in range(h)]

for i in range(h):
    streak = 0
    for j in range(1, w):
        if s[i][j]=='T' and s[i][j-1]=='T':
            s[i][j-1] = 'P'
            s[i][j] = 'C'
    print(*s[i], sep="")