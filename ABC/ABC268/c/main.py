n = int(input())
p = list(map(int, input().split()))

cnt = [0 for i in range(n)]
for i in range(n):
    cnt[(p[i]-i-1)%n] += 1; cnt[(p[i]-i)%n] += 1; cnt[(p[i]-i+1)%n] += 1

print(max(cnt))