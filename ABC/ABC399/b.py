n = int(input())
P = list(map(int, input().split()))

r = 1
rank = [-1 for i in range(n)]

while r <= n:
    max_idx = [i for i, v in enumerate(P) if v == max(P)]
    for i in range(len(max_idx)):
        P[max_idx[i]] = -1
        rank[max_idx[i]] = r
    r += len(max_idx)
    
for i in rank:
    print(i)