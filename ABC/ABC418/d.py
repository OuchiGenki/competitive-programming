n = int(input())
t = input()
dp = [0] * (n+1)
if t[0] == '1':
    dp[1] = 1

for i in range(1, n):
    if t[i] == '1':
        dp[i+1] += dp[i] + 1
    else:
        dp[i+1] += i-dp[i]

print(sum(dp))