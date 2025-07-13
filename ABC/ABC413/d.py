def solve():
    n = int(input())
    A = list(map(int, input().split()))
    s = set(A)

    if len(s) == 1:
        print('Yes')
        return 
    if len(s) == 2:
        p_cnt = len([a for a in A if a > 0])
        n_cnt = n - p_cnt
        listed_s = list(s)
        if listed_s[0] == -listed_s[1] and abs(p_cnt - n_cnt) <= 1:
            print('Yes')
            return

    A.sort(key=abs)
    flag = True
    for i in range(1, n-1):
        if A[i] ** 2 != A[i-1] * A[i+1]:
            flag = False
    if flag:
        print('Yes')
    else:
        print('No')


t = int(input())
for i in range(t):
    solve()