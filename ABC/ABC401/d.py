n, k = map(int, input().split())
S = list(input())
cnt_o = 0
for i in range(n):
    if S[i] == 'o':
        cnt_o += 1
    elif S[i] == '?':
        if i-1 >= 0 and S[i-1] == 'o':
            S[i] = '.'
        if i+1 < n and S[i+1] == 'o':
            S[i] = '.'

if cnt_o == k:
    for i in range(n):
        if S[i] == '?':
            S[i] = '.'
    print(''.join(S))
    exit()

cnt_o_max = cnt_o
q_streak = 0
for i in range(n):
    if S[i] == '?':
        q_streak += 1
    else:
        cnt_o_max += (q_streak + 1 ) // 2
        q_streak = 0
cnt_o_max += (q_streak + 1) // 2

if cnt_o_max > k:
    print(''.join(S))
    exit()

q_streak = 0
for i in range(n):
    if S[i] == '?':
        q_streak += 1
    else:
        if q_streak % 2 == 1:
            flag = True
            for i in range(i-1, i-q_streak-1, -1):
                if flag:    
                    S[i] = 'o'
                    flag = False
                else:
                    S[i] = '.'
                    flag = True
        q_streak = 0
if q_streak % 2 == 1:
    flag = True
    for i in range(i, i-q_streak, -1):
        if flag:    
            S[i] = 'o'
            flag = False
        else:
            S[i] = '.'
            flag = True

print(''.join(S))