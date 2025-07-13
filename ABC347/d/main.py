a, b, C = map(int, input().split())
cnt_0, cnt_1 = 0, 0
for i in range(60):
    if C & (1 << i):
        cnt_1 += 1
    else:
        cnt_0 += 1
if (((a + b) - cnt_1) % 2):
    print(-1)
    exit()
x = ((a + b) - cnt_1) // 2
if x > cnt_0 or x < 0:
    print(-1)
    exit()
a -= x
b -= x
if a + b != cnt_1 or a < 0 or b < 0:
    print(-1)
    exit()

X, Y = 0, 0
for i in range(60):
    if C & (1 << i):
        if a > 0:
            X += 2 ** i
            a -= 1
        else:
            if b > 0:
                Y += 2 ** i
                b -= 1
    else:
        if x > 0:
            X += 2 ** i
            Y += 2 ** i
            x -= 1

print(X, Y)