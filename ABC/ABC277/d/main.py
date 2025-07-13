n, m = map(int, input().split())
a = list(map(int, input().split()))

a.sort()
a += a
#print(a)

cum = [0]
for i in range(n*2):
    cum.append(cum[i]+a[i])
#print(cum)

r = 0
ans = 1 << 60
for l in range(n*2):
    while r-l+1 < n and r<2*n-1 and (a[r+1]==a[r] or a[r+1]==(a[r]+1)%m):
        r += 1
    #print(l, r)
    sum = cum[r+1] - cum[l]
    #print("res is", cum[n]-sum)
    ans = min(ans, cum[n]-sum)
    if l == r:
        r += 1

print(ans)