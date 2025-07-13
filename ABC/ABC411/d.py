N, Q = map(int, input().split())
query_list = [input().split() for _ in range(Q)]

ans = []
i = 0

for t in range(Q-1, -1, -1):
    query = query_list[t]
    if query[0] == '1':
        p = int(query[1])
        if i == p:
            i = 0
    elif query[0] == '2':
        p, s = int(query[1]), query[2]
        if i == p:
            ans.append(s[::-1])
    else:
        p = int(query[1])
        if i == 0:
            i = p

print(''.join(ans)[::-1])