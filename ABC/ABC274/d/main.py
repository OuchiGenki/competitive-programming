n, x, y = map(int, input().split())
A = list(map(int, input().split()))
dpx = [set() for _ in range(n+1)]
dpy = [set() for _ in range(n+1)]
dpx[1].add(A[0])
dpy[1].add(0)
for i in range(1, n):
    if i % 2:
        for j in dpy[i]:
            dpy[i+1].add(j + A[i])
            dpy[i+1].add(j - A[i])
        dpx[i+1] = dpx[i]
    else:
        for j in dpx[i]:
            dpx[i+1].add(j + A[i])
            dpx[i+1].add(j - A[i])
        dpy[i+1] = dpy[i]
if x in dpx[n] and y in dpy[n]:
    print('Yes')
else:
    print('No')