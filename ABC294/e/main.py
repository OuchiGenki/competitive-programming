import sys
sys.setrecursionlimit(10**8)
input = sys.stdin.readline

L, n1, n2 = map(int, input().split())
array1 = [] #[l, r, val]
array2 = []
before = 0
for i in range(n1):
    v, l = map(int, input().split())
    array1.append([before, before+l, v])
    before = before+l
before = 0
for i in range(n2):
    v, l = map(int, input().split())
    array2.append([before, before+l, v])
    before = before+l

p1 = p2 = 0
index1 = index2 = 0
cnt = 1
ans = 0
while cnt < n1+n2:
    L1, R1 = array1[index1][0], array1[index1][1]
    L2, R2 = array2[index2][0], array2[index2][1]

    if array1[index1][2] == array2[index2][2]:
        if min(R1, R2) - max(L1, L2) > 0:
            ans += min(R1, R2) - max(L1, L2)

    if R1 <= R2:
        index1 += 1
        cnt += 1
    else:
        index2 += 1
        cnt += 1


print(ans)