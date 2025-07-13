n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = set(list(map(int, input().split())))
x = int(input())

# dp[i] = -1...Cant Move, 1...OK, 0...NG
dp = [0 for i in range(x+1)]
dp[0] = 1

for i in range(x+1):
    if dp[i] != 1: continue
    for j in a:
        if i+j > x: continue
        if i+j not in b:
            dp[i+j] = 1
        else:
            dp[i+j] = -1

if dp[x] == 1:
    print("Yes")
else:
    print("No")