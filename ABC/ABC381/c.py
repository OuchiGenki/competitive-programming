N = int(input())
S = input()

max_cnt = 0
for i in range(N):
    if S[i] != '/':
        continue

    d = 1
    cnt = 0
    while i-d >= 0 and i+d < N:
        if S[i-d] == '1' and S[i+d] == '2':
            cnt += 1
        else:
            break
        d += 1
    max_cnt = max(max_cnt, cnt)

print(max_cnt * 2 + 1)