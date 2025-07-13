from collections import deque

h, w = map(int, input().split())
rs, cs = map(int, input().split())
rt, ct = map(int, input().split())
rs -= 1; cs -= 1; rt -= 1; ct -= 1
s = [input() for i in range(h)]

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]
INF = 1<<60
cnt = [[INF for i in range(w)] for j in range(h)]
visited = [[False for i in range(w)] for i in range(h)]
q = deque()

q.append((rs, cs))
visited[rs][cs] = True
cnt[rs][cs] = -1

while q:
    r, c = q.popleft()
    tmp = cnt[r][c] + 1

    for i in range(4):
        nr = r
        nc = c

        while True:
            nr += dr[i]
            nc += dc[i]

            if nr < 0 or nc < 0 or nr >= h or nc >= w:
                break
            if s[nr][nc] == '#':
                break
            if cnt[nr][nc] <= cnt[r][c]:
                break
            
            q.append((nr, nc))
            cnt[nr][nc] = tmp

if rs==rt and cs==ct:
    print(0)
else:
    print(cnt[rt][ct])