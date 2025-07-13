N = int(input())
D = list(map(int,input().split()))
for i in range(N-1):
    for j in range(i, N-1):
        print(sum(D[i:j+1]), end=' ')
    print()