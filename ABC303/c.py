N, M, H, K = map(int, input().split())
S = input()
item = set()
for i in range(M):
    x, y = map(int, input().split())
    item.add((x, y))

px, py = 0, 0
for i in range(N):
    H -= 1

    if S[i] == 'R':
        px += 1
    elif S[i] == 'L':
        px -= 1
    elif S[i] == 'U':
        py += 1
    elif S[i] == 'D':
        py -= 1
    
    if H < 0:
        print('No')
        exit()

    if (px, py) in item and H < K:
        item.remove((px, py))
        H = K

print('Yes')