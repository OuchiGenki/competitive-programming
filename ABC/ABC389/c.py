Q = int(input())
base = 0
base_idx = 0
snakes = [0]


for i in range(Q):
    query = list(map(int,input().split()))
    if query[0] == 1:
        l = query[1]
        snakes.append(l + snakes[-1])
    elif query[0] == 2:
        base += snakes[base_idx]
        base_idx += 1
    else:
        k = query[1]
        print(snakes[base_idx+k-1] - snakes[base_idx])
