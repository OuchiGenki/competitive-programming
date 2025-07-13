from bisect import bisect_right

N, Q = map(int, input().split())
R = list(map(int, input().split()))
R.sort()
cumsum = [0]
for i in range(N):
    cumsum.append(cumsum[i]+R[i])
cumsum.sort()

for i in range(Q):
    x = int(input())
    print(bisect_right(cumsum, x)-1)