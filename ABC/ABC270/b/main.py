x, y, z = map(int, input().split())

p = 0
hammer = False
flag = False

if 0 < x:
    while p != x:
        if p == z:
            hammer = True
        if p == y:
            if hammer == False:
                p = -2*z + x
                if p < 0:
                    print(-1)
                else:
                    print(p)
                exit()
        p += 1
    print(p)

else:
    while p != x:
        if p == z:
            hammer = True
        if p == y:
            if hammer == False:
                p = 2*z - x
                if p < 0:
                    print(-1)
                else:
                    print(p)
                exit()
        p -= 1
    print(p)