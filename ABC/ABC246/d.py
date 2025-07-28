def calc(a, b):
    return a**3 + a**2*b + a*b**2 + b**3

n = int(input())
a = 0
res = []
while True:
    ng = -1
    ok = 10**6
    while ok - ng > 1:
        b = (ng + ok) // 2
        if calc(a, b) >= n:
            ok = b
        else:
            ng = b
    if a > ok:
        break
    res.append(calc(a, ok))
    a += 1
print(min(res))