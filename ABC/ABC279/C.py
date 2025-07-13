h, w = map(int, input().split())
s = [input() for i in range(h)]
t = [input() for i in range(h)]

trans_s = []
trans_t = []

for i in range(w):
    sl = []
    tl = []
    for j in range(h):
        sl.append(s[j][i])
        tl.append(t[j][i])
    trans_s.append(sl)
    trans_t.append(tl)

if sorted(trans_s) == sorted(trans_t):
    print("Yes")
else:
    print("No")