n = int(input())
a = list(map(int, input().split()))

odd = []
even = []
for i in range(n):
    if a[i] % 2:
        odd.append(a[i])
    else:
        even.append(a[i])

odd.sort(reverse=True)
even.sort(reverse=True)

if len(odd) < 2 and len(even) < 2:
    print(-1)
    exit()

res1 = res2 = 0
if len(odd) >= 2:
    res1 = odd[0] + odd[1]
if len(even) >= 2:
    res2 = even[0] + even[1]

if res1 > res2:
    print(res1)
else:
    print(res2)