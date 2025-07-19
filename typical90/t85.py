k = int(input())
lst = [i for i in range(1, 10**6+1) if k % i == 0]
ans = 0
for a in range(1, 10**4+1):
    if k % a != 0:
        continue
    for b in lst:
        if a > b or k % (a*b) != 0:
            continue
        c = k // (a*b)
        if c >= b:
            ans += 1
print(ans)