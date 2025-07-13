import math

n = int(input())
ans = 0
for i in range(1, n):
    ab = i
    cd = n-i
    s1 = 0
    s2 = 0
    for j in range(1, int(ab**0.5)+1):
        if ab%j == 0:
            if j==ab**0.5:
                s1 += 1
            else:
                s1 += 2
    for j in range(1, int(cd**0.5)+1):
        if cd%j == 0:
            if j==cd**0.5:
                s2 += 1
            else:
                s2 += 2
    ans += s1*s2
print(ans)