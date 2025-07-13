n, q = map(int, input().split())
a = list(map(int, input().split()))

base = 0
for i in range(q):
    li = list(map(int, input().split()))
    t, x, y = li
    x -= 1
    y -= 1
    
    if t == 1:
        a[(base+x)%n], a[(base+y)%n] = a[(base+y)%n], a[(base+x)%n]
    elif t == 2:
        base = (base-1)%n
    else:
        print(a[(base+x)%n])