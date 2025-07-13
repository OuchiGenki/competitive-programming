n = int(input())
S = input()
mp = [0 for i in range(10)]
for i in range(n):
    mp[int(S[i])] += 1
x = 0
ans = 0
while x * x < 10**n:
    t = str(x * x)
    mp2 = [0 for i in range(10)]
    for i in range(len(t)):
        mp2[int(t[i])] += 1
    flag = True
    for i in range(1, 10):
        if mp[i] != mp2[i]:
            flag = False
    if flag:
        ans += 1
    x += 1
print(ans)