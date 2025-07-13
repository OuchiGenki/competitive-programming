from itertools import permutations

def dist(x1, y1, x2, y2):
    return ((x1-x2)**2 + (y1-y2)**2)**0.5

N, S, T = map(int, input().split())
ABCD = []
for i in range(N):
    ABCD.append(list(map(int, input().split())))

ans = float('inf')
for v in permutations(range(N)):
    for i in range(2**N):
        px, py = 0, 0
        tmp = 0
        for j in range(N):
            a = ABCD[v[j]][0]
            b = ABCD[v[j]][1]
            c = ABCD[v[j]][2]
            d = ABCD[v[j]][3]
            if i & (1 << j):
                tmp += dist(px, py, a, b) / S
                tmp += dist(a, b, c, d) / T
                px, py = c, d
            else:
                tmp += dist(px, py, c, d) / S
                tmp += dist(c, d, a, b) / T
                px, py = a, b
        ans = min(ans, tmp)

print(ans)