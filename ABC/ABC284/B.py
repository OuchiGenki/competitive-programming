t = int(input())
for i in range(t):
    n = int(input())
    test = list(map(int, input().split()))
    ans = 0
    for j in test:
        if j%2==1:
            ans+=1
    print(ans)