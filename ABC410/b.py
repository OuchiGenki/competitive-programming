from collections import defaultdict

N, Q = map(int, input().split())
ball = defaultdict(int)
box = [0 for i in range(N)]
X = list(map(int, input().split()))
for i in range(Q):
    if X[i] >= 1:
        ball[i] = X[i]-1
        box[X[i]-1] += 1
    else:
        ball[i] = box.index(min(box))
        box[box.index(min(box))] += 1
print(*list(map(lambda x: x+1, ball.values())))