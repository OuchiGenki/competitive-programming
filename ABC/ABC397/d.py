def f(c, d):
    return (-d + (d ** 2 - 4 * c) ** 0.5) / 2

N = int(input())
for d in range(1, int(N**(1/3))+1):
    c = (d ** 3 - N) / (3 * d)
    y = int(f(c, d))
    if y * y + d * y + c == 0:
        print(y + d, y)
        exit()

print(-1)