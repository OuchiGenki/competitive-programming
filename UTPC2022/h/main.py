import sys
import copy
sys.setrecursionlimit(10**8)
input = sys.stdin.readline
mod = 998244353

n = input()
a = []
for i in range(len(n)-1):
    a.append(int(n[i]))
dig = len(a)

min_num = min(a)

ind = 0
min_n = 10
min_ind = []
for i in range(dig):
    if a[i] == min_num:
        min_ind.append(i)

sum = 0
res = 0
cnt = 0

for i in min_ind:
    res = (9-a[i])*pow(10, dig-i-1, mod)
    print("add", res)
    sum += res
    sum %= mod
    cnt += 1

for i in range(min_ind[-1]+1, dig):
    res = (9-a[i])*pow(10, dig-i-1, mod)
    print("add", res)
    sum += res
    sum %= mod
    cnt += 1

e = pow(pow(10, dig-min_ind[0], mod), -1, mod)
print(sum)
print(sum*e%mod)