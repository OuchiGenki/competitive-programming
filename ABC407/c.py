S = list(input())
N = len(S)
res = 0
cnt = 0
for i in range(N-1, -1, -1):
    res += (int(S[i])-cnt)%10
    cnt += (int(S[i])-cnt)%10
res += N
print(res)