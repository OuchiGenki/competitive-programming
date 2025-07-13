a, b, c, x, y = map(int, input().split())
inf = 1 << 60
res1 = a*x + b*y
res2 = inf; res3 = inf; res4 = inf; res5 = inf
if x <= y:
    res2 = 2*c*x + b*(y-x)
    res3 = 2*c*y
else:
    res4 = 2*c*x
    res5 = 2*c*y + a*(x-y)
print(min(res1, res2, res3, res4, res5))