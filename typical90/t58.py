n, k = map(int, input().split())
visited = [False] * 10**5
visited[n] = True
p = [n]
x = n
while True:
    y = sum(list(map(int, str(x))))
    z = (x + y) % 10**5
    if visited[z]:
        si = p.index(z)
        l = len(p) - si
        break
    visited[z] = True
    p.append(z)
    x = z

if k < len(p):
    print(p[k])
else:
    k -= si
    print(p[si + k % l])