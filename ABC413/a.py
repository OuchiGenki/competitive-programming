n, m = map(int, input().split())
A = list(map(int, input().split()))
if sum(A) <= m:
    print('Yes')
else:
    print('No')