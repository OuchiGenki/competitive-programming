from math import log2

def f(n):
    cnt = 0
    while n > 0 and n % 2 == 0:
        n //= 2
        cnt += 1
    return cnt

l, r = map(int, input().split())
ans = []
while l != r:
    if l == 0:
        i = 0
        while 2**i <= r:
            i += 1
        ans.append((0, 2**(i-1)))
        l = 2**(i-1)
        continue


    i = f(l)
    j = l // 2**i

    while 2**i * (j + 1) > r:
        i -= 1
        j = l // 2**i

    ans.append((2**i * j, 2**i * (j+1)))
    l = 2**i * (j + 1)

print(len(ans))
for row in ans:
    print(*row)