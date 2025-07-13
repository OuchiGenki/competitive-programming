n = int(input())
x = list(map(int, input().split()))
x.sort()
x = x[:-n]
x.sort(reverse=True)
x = x[:-n]
ans = 0
for i in x:
    ans += i
print('{:.7f}'.format(ans/len(x)))