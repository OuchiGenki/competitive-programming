import sys
sys.setrecursionlimit(10**8)
input = sys.stdin.readline

s = [input() for i in range(8)]
for i in range(8):
    for j in range(8):
        if s[i][j]=='*':
            print(chr(97+j), 8-i, sep="")
            break