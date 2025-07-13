n = int(input())
a = list(map(int, input().split()))
q = int(input())
t = list(map(int, input().split()))
s = set()

for j in range(2**n):
    cnt = 0
    for k in range(n):
        if j>>k & 1:
            cnt += a[k]
    s.add(cnt)

for i in range(q):
    if t[i] in s:
        print("yes")
    else:
        print("no")