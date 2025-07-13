n, q = map(int, input().split())
a = []
for i in range(n):
    li = list(map(int, input().split()))
    a.append(li[1:li[0]+1])
for i in range(q):
    s, t = map(int, input().split())
    print(a[s-1][t-1])