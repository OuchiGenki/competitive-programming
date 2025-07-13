N, S = map(int, input().split())
T = list(map(int, input().split()))
T = [0] + T

flag = True
for i in range(1, N+1):
    if T[i] - T[i-1] >= S+0.5:
        flag = False

if flag:
    print('Yes')
else:
    print('No')