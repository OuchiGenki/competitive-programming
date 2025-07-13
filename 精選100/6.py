n = int(input())
s = input()

ans = set()
a = 2
for i in range(1000):
    num = str(i).zfill(3)
    p = 0
    for j in range(n):
        if s[j] == num[p]:
            p += 1
        if p == len(num):
            ans.add(num)
            break

print(len(ans))