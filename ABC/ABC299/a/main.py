import sys
sys.setrecursionlimit(10**8)
input = sys.stdin.readline

n = int(input())
s = input()

flag = False
for i in range(n):
    if flag and s[i]=='|':
        print("out")
        exit()
    if flag and s[i]=='*':
        print("in")
        exit()
    if s[i] == '|':
        flag = True