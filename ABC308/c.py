N = int(input())
ls = []
for i in range(N):
    a, b = map(int, input().split())
    ls.append((a * 10 ** 100 // (a+b), -(i+1)))
ls.sort(reverse=True)

ans = []
for i in range(N):
    ans.append(-ls[i][1])
print(*ans)