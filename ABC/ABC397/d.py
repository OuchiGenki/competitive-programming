n = int(input())
for k in range(1, 10**6+1):
    if (k**3 - n) % (3*k) != 0:
        continue
    c = (k**3 - n) // (3*k)
    y = (-k + (k**2 - 4*c)**0.5) / 2
    if k**2-4*c >= 0 and y.is_integer() and y > 0:
        x = y + k
        print(int(x), int(y))
        exit()
print(-1)