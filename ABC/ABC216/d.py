from collections import deque, defaultdict

n, m = map(int, input().split())
A = []
cnt = defaultdict(int)
idx = defaultdict(list)
que = deque()
for i in range(m):
    k = int(input())
    a = deque(map(int, input().split()))
    A.append(a)
    cnt[a[0]] += 1
    if cnt[a[0]] == 2:
        que.append(a[0])
    for j in range(k):
        idx[a[j]].append(i)

op = 0
while que:
    x = que.popleft()
    cnt[x] -= 2
    op += 2
    idx1, idx2 = idx[x]
    A[idx1].popleft()
    A[idx2].popleft()
    if A[idx1]:
        cnt[A[idx1][0]] += 1
        if cnt[A[idx1][0]] == 2:
            que.append(A[idx1][0])
    if A[idx2]:
        cnt[A[idx2][0]] += 1
        if cnt[A[idx2][0]] == 2:
            que.append(A[idx2][0])

if op < 2*n:
    print('No')
else:
    print('Yes')
