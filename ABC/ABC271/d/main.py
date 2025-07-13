n, s = map(int, input().split())
A = []
B = []
dp = [[False for i in range(s+1)] for j in range(n+1)]
dp[0][0] = True

for i in range(n):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)
    for j in range(s+1):
        if dp[i][j]:
            if j+a <= s:
                dp[i+1][j+a] = True
            if j+b <= s:
                dp[i+1][j+b] = True

if dp[n][s] == False:
    print("No")
    exit()
print("Yes")

ans = []
pos = s
for i in range(n):
    if dp[n-i-1][pos-A[n-i-1]]:
        ans.append('H')
        pos -= A[n-i-1]
        continue
    if dp[n-i-1][pos-B[n-i-1]]:
        ans.append('T')
        pos -= B[n-i-1]
ans.reverse()
for i in range(n):
    print(ans[i], end="")
print()