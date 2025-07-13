T = int(input())
for _ in range(T):
    test = int(input())
    for i in range(2, int(test**(1/3))+1):
        if test % i == 0:
            if test % (i**2) == 0:
                p = i
                q = test // p**2
            else:
                q = i
                p = (test // q) ** 0.5
            break
    print(int(p), int(q))
