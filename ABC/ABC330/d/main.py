N = int(input())
S = [input() for i in range(N)]

sum_r = [0 for i in range(N)]
sum_c = [0 for i in range(N)]

for i in range(N):
    for j in range(N):
        if S[i][j] == 'o':
            sum_r[i] += 1
            sum_c[j] += 1

ans = 0
for i in range(N):
    for j in range(N):
        if S[i][j] == 'x':
            continue
        ans += (sum_r[i] - 1) * (sum_c[j] - 1)

print(ans)