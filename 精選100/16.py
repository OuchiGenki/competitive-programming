from itertools import *
n = int(input())
p = tuple(map(int, input().split()))
q = tuple(map(int, input().split()))
t = (i+1 for i in range(n))

a = b = 0
cnt = 0
for i in permutations(t):
    cnt += 1
    if i==p:
        a = cnt
    if i==q:
        b = cnt

print(abs(a-b))