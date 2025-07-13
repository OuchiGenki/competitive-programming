import sys
sys.setrecursionlimit(10**8)

a = [list(map(int, input().split())) for i in range(9)]
flag = 0

for i in range(9):
    rs = set()
    cs = set()
    for j in range(9):
        rs.add(a[i][j])
        cs.add(a[j][i])
    if len(rs)!=9 or len(cs)!=9:
        flag=1

for si in range(3):
    for sj in range(3):
        rb = set()
        for i in range(3):
            for j in range(3):
                r = 3*si+i
                c = 3*sj+j
                rb.add(a[r][c])
        if len(rb)!=9:
            flag = 1

if flag:
    print("No")
else:
    print("Yes")