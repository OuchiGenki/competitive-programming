import sys
sys.setrecursionlimit(10**8)

n =int(input())
s = input()

for i in range(n-2):
    if s[i:i+3] == "ABC":
        print(i+1)
        exit()

print(-1)