n, p, q, r = map(int, input().split())
A = list(map(int, input().split()))
rightP, rightQ, rightR = 0, 0, 0
sumP, sumQ, sumR = 0, 0, 0
resP, resQ, resR = [], [], []
s1 = set()
s2 = set()
for left in range(n):
    while rightP < n and sumP + A[rightP] <= p:
        sumP += A[rightP]
        rightP += 1
    while rightQ < n and sumQ + A[rightQ] <= q:
        sumQ += A[rightQ]
        rightQ += 1
    while rightR < n and sumR + A[rightR] <= r:
        sumR += A[rightR]
        rightR += 1

    if sumP == p:
        resP.append((left, rightP-1))
        s1.add(rightP-1)
    if sumQ == q:
        resQ.append((left, rightQ-1))
    if sumR == r:
        s2.add(left)
        resR.append((left, rightR-1))

    if left == rightP:
        rightP += 1
    else:
        sumP -= A[left]
    if left == rightQ:
        rightQ += 1
    else:
        sumQ -= A[left]
    if left == rightR:
        rightR += 1
    else:
        sumR -= A[left]

ans = 'No'
for lq, rq in resQ:
    if resP and resR and lq-1 in s1 and rq + 1 in s2:
        ans = 'Yes'
print(ans)