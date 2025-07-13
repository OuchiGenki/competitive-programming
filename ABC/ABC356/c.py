N, M, K = map(int, input().split())
C = []
A = []
R = []
for i in range(M):
    li = list(input().split())
    C.append(int(li[0]))
    A.append(list(map(lambda x: int(x)-1, li[1:C[i]+1])))
    R.append(li[-1])

ans = 0
for i in range(2**N):
    flag = True

    for j in range(M):
        cnt1 = 0
        for k in range(C[j]):
            if i & (1 << A[j][k]):
                cnt1 += 1
        if cnt1 >= K and R[j] == 'x':
            flag = False
        elif cnt1 < K and R[j] == 'o':
            flag = False
    
    if flag:
        ans += 1

print(ans)