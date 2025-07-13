def f(x):
    return int(x)%46

n = int(input())
a = list(map(f, input().split()))
b = list(map(f, input().split()))
c = list(map(f, input().split()))

cntA = [0 for i in range(46)]
cntB = [0 for i in range(46)]
cntC = [0 for i in range(46)]

for i in range(n):
    cntA[a[i]] += 1
    cntB[b[i]] += 1
    cntC[c[i]] += 1

ans = 0
for i in range(0, 46):
    for j in range(0, 46):
        for k in range(0, 46):
            if (i+j+k) % 46 == 0:
                ans += cntA[i]*cntB[j]*cntC[k]

print(ans)