import sys
sys.setrecursionlimit(10**8)

n = int(input())
a = list(map(int,input().split()))

ans = n
left = 0
right = 1
while right < n:
    d = a[right]-a[left]
    while right<n and a[right]-a[right-1]==d:
        right += 1
    ans += (right-left)*(right-left-1)//2
    left = right-1

print(ans)