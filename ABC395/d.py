N, Q = map(int, input().split())
pigeon = [i for i in range(N)]
nest = [i for i in range(N)]
nest_idx = {i:i for i in range(N)}

for i in range(Q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        a, b = query[1]-1, query[2]-1
        idx = nest_idx[b]
        pigeon[a] = idx
    elif query[0] == 2:
        a, b = query[1]-1, query[2]-1
        nest_a_idx = nest_idx[a]
        nest_b_idx = nest_idx[b]
        nest[nest_a_idx], nest[nest_b_idx] = nest[nest_b_idx], nest[nest_a_idx]
        nest_idx[a], nest_idx[b] = nest_idx[b], nest_idx[a]
    else:
        a = query[1]-1
        print(nest[pigeon[a]] + 1)