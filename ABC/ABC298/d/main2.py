import sys
sys.setrecursionlimit(10**8)

q = int(input())
s = [1]
n = 1
begin = 0
MOD = 998244353

for i in range(q):
    li = list(map(int, input().split()))
    case = li[0]

    if case == 1:
        x = li[1]
        s.append(x)
        n = n*10+x
        n %= MOD
    elif case == 2:
        n -= s[begin]*pow(10, len(s)-1-begin, MOD)
        begin += 1
        n %= MOD
    elif case == 3:
        print(n)