def f(x):
    return B*x + A/((x+1)**0.5)

A, B = map(int, input().split())
ans = float('inf')
base = int((A/(2*B)) ** (2/3) - 1)
for x in range(max(0, base-3), base+4):
    ans = min(ans, f(x))
print(ans)