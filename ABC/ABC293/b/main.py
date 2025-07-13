n = int(input())
a = list(map(int, input().split()))
called = [False for i in range(n)]
for i in range(n):
    if called[i] == False:
        called[a[i]-1] = True
ans = []
for i in range(n):
    if called[i] == False:
        ans.append(i+1)
print(len(ans))
print(*ans)