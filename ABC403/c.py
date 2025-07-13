from collections import defaultdict

N, M, Q = map(int, input().split())
root = [False for i in range(N+1)]
s = defaultdict(set)

for i in range(Q):
    li = list(map(int, input().split()))
    if li[0] == 1:
        X, Y = li[1], li[2]
        s[X].add(Y)
    elif li[0] == 2:
        X = li[1]
        root[X] = True
    elif li[0] == 3:
        X, Y = li[1], li[2]
        if root[X]:
            print("Yes")
            continue
        if Y in s[X]:
            print("Yes")
        else:
            print("No")
