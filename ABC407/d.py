H, W = map(int, input().split())
A = [list(map(int, input().split())) for i in range(H)]

horizontal_domino = 3
vertical_domino = 1 << W | 1

possible_domino = [0]
for i in range(H):
    for j in range(W):
        bit = i*W + j
        for domino in possible_domino:
            if j < W-1 and not(domino & (horizontal_domino << bit)):
                possible_domino.append(domino | (horizontal_domino << bit))
            if i < H-1 and not(domino & (vertical_domino << bit)):
                possible_domino.append(domino | (vertical_domino << bit))

ans = 0
for domino in possible_domino:
    tmp = 0
    for i in range(H):
        for j in range(W):
            bit = i*W + j
            if not(domino & (1 << bit)):
                tmp ^= A[i][j]
    ans = max(ans, tmp)

print(ans)