n, k = map(int, input().split())
num = [-1 for i in range(10**5+1)]
MOD = 10**5
ls = [n]
d = dict()


x = n
key = 0
for i in range(k):
    y = sum(list(map(int, str(x))))
    z = (x + y) % MOD

    if z in d:
        start = d[z]
        ls = ls[start:]
        print(ls[(k-start)%len(ls)])
        exit()

    ls.append(z)
    d[x] = i
    x = z

print(ls[k])