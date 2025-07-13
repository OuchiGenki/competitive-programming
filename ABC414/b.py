n = int(input())
ans = ''
for i in range(n):
    c, l = input().split()
    l = int(l)
    if len(ans) + l > 100:
        print('Too Long')
        exit()
    while l > 0:
        ans += str(c)
        l -= 1
print(ans)