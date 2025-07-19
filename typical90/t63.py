from collections import defaultdict

def maximum_same(R):
    d = defaultdict(int)
    ret = 0
    for r in R:
        d[r] += 1
        ret = max(ret, d[r])
    return ret
    

h, w = map(int, input().split())
P = [list(map(int, input().split())) for _ in range(h)]
ans = 0
for v in range(2**h):
    R = []
    for i in range(w):
        num = -1
        flag = True
        for j in range(h):
            if not v & (1 << j):
                continue
            if num == -1:
                num = P[j][i]
            if P[j][i] != num:
                flag = False
        if flag:
            R.append(num)
    cnt_W = maximum_same(R)
    cnt_H = v.bit_count()
    ans = max(ans, cnt_W * cnt_H)
print(ans)