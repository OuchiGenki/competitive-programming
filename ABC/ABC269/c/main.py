n = int(input())

cnt = 0
mul = []
for i in range(65):
    if (n >> i) & 1:
        mul.append(i)
        cnt += 1

for i in range(2**cnt):
    ans = 0
    for j in range(cnt):
        if (i>>j) & 1:
            ans += 2**mul[j]
    print(ans)
