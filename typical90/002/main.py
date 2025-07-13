def show(x):
    for i in range(n-1, -1, -1):
        if x >> i & 1:
            print(')', end="")
        else:
            print('(', end="")

n = int(input())
for i in range(2**n):
    cnt0 = 0
    cnt1 = 0
    skip = False
    for j in range(n-1, -1, -1):
        if i >> j & 1:
            cnt1 += 1
        else:
            cnt0 += 1
        if cnt1 > cnt0:
            skip = True
    if skip:
        continue
    if cnt0 != cnt1:
        continue
    show(i)
    print()