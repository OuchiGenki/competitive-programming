import copy

N = int(input())
max_X = 0
min_X = 0
L, R = [], []
for i in range(N):
    l, r = map(int, input().split())
    L.append(l)
    R.append(r)
    max_X += r
    min_X += l

if min_X > 0 or max_X < 0:
    print('No')
    exit()

ans = copy.deepcopy(L)
sum = sum(ans)
for i in range(N):
    d = min(R[i] - L[i], -sum)
    sum += d
    ans[i] += d

print('Yes')
print(*ans)