import sys
sys.setrecursionlimit(10**8)

n = int(input())
for i in range(n, 1000):
    s = str(i)
    if int(s[0])*int(s[1])==int(s[2]):
        print(s)
        break