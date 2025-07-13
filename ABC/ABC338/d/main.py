import sys
sys.setrecursionlimit(10**8)

n, m = map(int, input().split())
x = list(map(lambda x:int(x)-1, input().split()))
v = [0 for i in range(n)]

for i in range(m-1):
    a = x[i+1]
    b = x[i]
    if a > b:
        a, b = b, a
    r = (b-a)%n
    l = (a-b)%n
    v[a] += l
    v[b] -= l
    v[b] += r
    v[0] += r
    v[a] -= r

for i in range(n-1):
    v[i+1] += v[i]

print(min(v))
