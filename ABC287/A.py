n = int(input())
s = [input() for i in range(n)]
cnt = 0
for i in range(n):
    if s[i] == "For":
        cnt += 1
if cnt >= n//2+1:
    print("Yes")
else:
    print("No")