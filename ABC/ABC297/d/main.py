import sys
sys.setrecursionlimit(10**8)
input = sys.stdin.readline

a, b = map(int, input().split())

ans = 0
while a!=b:
    if a>b:
        if a%b == 0:
            ans += (a-b)//b
            break
        q = a//b
        a -= q*b
        ans += q
    else:
        if b%a == 0:
            ans += (b-a)//a
            break
        q = b//a
        b -= q*a
        ans += q

print(ans)