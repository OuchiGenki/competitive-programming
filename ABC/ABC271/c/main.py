n = int(input())
a = list(map(int, input().split()))
have = [False for i in range(n+2)]

wild = 0
for i in range(n):
    if a[i] > n:
        wild += 1
        continue
    if have[a[i]] == True:
        wild += 1
    else:
        have[a[i]] = True

l = 1
r = n

while True:
    while have[l] == True:
        l += 1
    while have[r] == False and r != 0:
        r -= 1
    if wild - 2 >= 0:
        wild -= 2
        have[l] = True
    else:
        if l >= r:
            break
        wild += 1
        have[r] = False

print(l-1)