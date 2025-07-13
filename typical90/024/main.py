n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
cnt = 0
for i in range(n):
    cnt += abs(a[i]-b[i])
if k%2 == cnt%2 and cnt <= k:
    print("Yes")
else:
    print("No")