N = int(input())
ls = []
res = 0
x = 1
while x**3 <= N:
    k = str(x**3)
    if k == k[::-1]:
        res = max(res, int(k))
    x += 1

print(res)