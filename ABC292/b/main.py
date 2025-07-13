n, q = map(int, input().split())
p = [0 for i in range(n)]
for i in range(q):
    c, x = map(int, input().split())
    if c == 1:
        p[x-1] += 1
    elif c == 2:
        p[x-1] += 2
    else:
        if p[x-1] >= 2:
            print("Yes")
        else:
            print("No")