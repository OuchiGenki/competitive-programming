n = int(input())
X, Y = [], []
for _ in range(n):
    x, y = map(int, input().split())
    X.append(x)
    Y.append(y)
X.sort()
Y.sort()
if n % 2:
    a = X[n//2]
    b = Y[n//2]
else:
    a = (X[n//2 - 1] + X[n//2]) / 2
    b = (Y[n//2 - 1] + Y[n//2]) / 2

ans = 0
for i in range(n):
    ans += abs(X[i] - a) + abs(Y[i] - b)
print(int(ans))