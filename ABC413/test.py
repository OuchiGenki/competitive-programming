from random import randint

def solve():
    n = randint(2, 100000)
    A = [randint(-10**9, 10**9) for _ in range(n)]
    if n == 2:
        print('Yes')
        return
    A.sort(key=lambda x: abs(x))

    flag = True
    pm = -1
    cntm = 0
    for i in range(n):
        if A[i] < 0:
            if pm != 0:
                flag = False
            pm = 1
            cntm += 1
        else:
            if pm == 0:
                flag = False
            pm = 0

    flag2 = True
    for i in range(1, n-1):
        if abs(A[i]) ** 2 != abs(A[i-1]) * abs(A[i+1]):
            flag2 = False
            break

    if cntm == 0 or cntm == n:
        if flag2:
            print('Yes')
        else:
            print('No')
    else:
        if flag and flag2:
            print('Yes')
        else:
            print('No')


while True:
    solve()