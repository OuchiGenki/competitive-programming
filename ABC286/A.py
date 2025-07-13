n, p, q, r, s = map(int, input().split())
a = list(map(int, input().split()))

for i in range(q-p+1):
    a[p-1+i], a[r-1+i] = a[r-1+i], a[p-1+i]

for ans in a:
    print(ans, end=" ")