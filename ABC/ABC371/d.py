from bisect import bisect_left, bisect_right

N = int(input())
X = list(map(int, input().split()))
P = list(map(int, input().split()))
Q = int(input())

cumsum = [0]
for i in range(N):
    cumsum.append(cumsum[-1] + P[i])

ans = []
for i in range(Q):
    l, r = map(int, input().split())
    i = bisect_left(X, l)
    j = bisect_right(X, r)
    ans.append(cumsum[j] - cumsum[i])

for i in ans:
    print(i)