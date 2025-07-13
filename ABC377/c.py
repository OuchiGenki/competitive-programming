N, M = map(int, input().split())
s = set()
for i in range(M):
    a, b = map(int, input().split())
    s.add((a, b))
    for da, db in [(2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2), (1, -2), (2, -1)]:
        na = a + da
        nb = b + db
        if na < 1 or na > N or nb < 1 or nb > N:
            continue
        s.add((na, nb))
print(N*N - len(s))