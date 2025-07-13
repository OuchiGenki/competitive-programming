n, k = map(int, input().split())
a, b = [], []
for i in range(n):
    A, B = map(int, input().split())
    a.append(A-B)
    b.append(B)

ab = sorted(a+b, reverse=True)

ans = 0
for i in range(k):
    ans += ab[i]
print(ans)