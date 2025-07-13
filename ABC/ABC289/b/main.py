from collections import deque

n, m = map(int, input().split())
a = list(map(int, input().split()))
d = deque()
ans = []

s = set()
for i in range(m):
    s.add(a[i]-1)

for i in range(n):
    if i in s:
        d.append(i)
    else:
        d.append(i)
        while len(d)!=0:
            ans.append(d.pop()+1)
while len(d)!=0:
    ans.append(d.pop()+1)

print(*ans)