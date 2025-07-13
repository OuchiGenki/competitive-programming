N, Q = map(int, input().split())
pos = []
ans = []

for i in range(N):
    pos.append((N-i, 0))

for i in range(Q):
    query = list(input().split())
    
    if query[0] == '1':
        c = query[1]
        if c == 'R':
            pos.append((pos[-1][0] + 1, pos[-1][1]))
        if c == 'L':
            pos.append((pos[-1][0] - 1, pos[-1][1]))
        if c == 'U':
            pos.append((pos[-1][0], pos[-1][1] + 1))
        if c == 'D':
            pos.append((pos[-1][0], pos[-1][1] - 1))

    elif query[0] == '2':
        p = int(query[1])
        ans.append(pos[-p])

for row in ans:
    print(*row)