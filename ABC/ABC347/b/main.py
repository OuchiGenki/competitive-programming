import sys
sys.setrecursionlimit(10**8)

s = input()
n = len(s)
ans = set()

for i in range(1,n+1):
    for j in range(n):
        ans.add(s[j:j+i])

print(len(ans))