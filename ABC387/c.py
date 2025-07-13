def f(d):
    result = 0
    d = list(map(int, list(str(d))))
    n = len(d)

    #case1
    flag = True
    for i in range(1, n):
        if d[0] <= d[i]:
            flag = False
    if flag:
        result += 1
    
    #case2
    tmp = 0
    for i in range(1, n):   #どこまで同じか
        result += min(d[0], d[i]) * d[0]**(n-i-1)
        tmp += min(d[0], d[i]) * d[0]**(n-i-1)
        if d[0] <= d[i]:
            break
    
    #case3
    tmp = 0
    for i in range(1, d[0]):
        result += i**(n-1)
        tmp += i**(n-1)
    
    #case4
    tmp = 0
    for k in range(1, n):   #桁数
        for i in range(1, 10):  #先頭の数字
            result += i**(k-1)
            tmp += i**(k-1)

    return result
        

L, R = map(int, input().split())
print(f(R) - f(L-1))