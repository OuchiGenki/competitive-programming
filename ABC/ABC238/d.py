T = int(input())
for _ in range(T):
    a, s = map(int, input().split())
    t = s
    for i in range(60):
        if a & (1 << i):
            t -= 2 * (1 << i)
    if t < 0:
        print('No')
        continue

    flag = False
    for i in range(59, -1, -1):
        if a & (1 << i):
            continue
        if t - (1 << i) >= 0:
            t -= (1 << i)
        if t == 0:
            flag = True
            break
    if flag:
        print('Yes')
    else:
        print('No')