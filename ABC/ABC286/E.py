from collections import deque

n = int(input())
a = list(map(int, input().split()))
s = [list(input()) for i in range(n)]
q = int(input())

dist = [[-1 for i in range(n)] for j in range(n)]
value = [[0 for i in range(n)] for j in range(n)]

for i in range(n):
    value[i][i] = a[i]

for i in range(n):
    que = deque()
    que.append(i)
    dist[i][i] = 0

    while len(que) > 0:
        pos = que.popleft()

        for next_pos in range(n):
            if s[pos][next_pos] == 'N': continue
            if dist[i][next_pos] == dist[i][pos] + 1 and value[i][pos]+a[next_pos] > value[i][next_pos]:
                value[i][next_pos] = value[i][pos]+a[next_pos]
            if dist[i][next_pos] != -1: continue
            dist[i][next_pos] = dist[i][pos] + 1
            value[i][next_pos] = value[i][pos] + a[next_pos]
            que.append(next_pos)

for i in range(q):
    u, v = map(int, input().split())
    if dist[u-1][v-1] == -1:
        print("Impossible")
    else:
        print(dist[u-1][v-1], value[u-1][v-1])