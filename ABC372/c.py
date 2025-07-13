N, Q = map(int, input().split())
S = list(input())
cnt = 0
for i in range(1, N-1):
    if S[i-1:i+2] == ['A', 'B', 'C']:
        cnt += 1

def check(i):
    flag = False
    if 0 <= i-2 and S[i-2:i+1] == ['A', 'B', 'C']:
        flag = True
    if 0 <= i-1 and i+1 < N and S[i-1:i+2] == ['A', 'B', 'C']:
        flag = True
    if i+2 < N and S[i:i+3] == ['A', 'B', 'C']:
        flag = True
    return flag

for i in range(Q):
    x, c = input().split()
    x = int(x)-1
    if check(x):
        S[x] = c
        if not check(x):
            cnt -= 1
            print(cnt)
        else:
            print(cnt)
    else:
        S[x] = c
        if check(x):
            cnt += 1
            print(cnt)
        else:
            print(cnt)
