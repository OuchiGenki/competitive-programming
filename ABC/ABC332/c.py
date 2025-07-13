N, M = map(int, input().split())
S = input()
num_t = M

for num_at in range(N+1):
    cnt1 = num_t
    cnt2 = num_at
    flag = True

    for i in range(N):
        if S[i] == '0':
            cnt1 = num_t
            cnt2 = num_at
        if S[i] == '1':
            if cnt1 > 0:
                cnt1 -= 1
            else:
                cnt2 -= 1
        if S[i] == '2':
            cnt2 -= 1
        
        if cnt1 < 0 or cnt2 < 0:
            flag = False

    if flag:
        print(num_at)
        exit()