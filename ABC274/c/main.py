n = int(input())
a = list(map(int, input().split()))
gen = [0 for i in range(2*(n+1)+1)]

for i in range(1, n+1):
    gen[i*2] = gen[a[i-1]] + 1
    gen[i*2+1] = gen[a[i-1]] + 1

for i in range(1, 2*n+2):
    print(gen[i])