import itertools
n = int(input())
p = list(map(int, input().split()))
p.reverse()

for i in range(n-1):
    if p[i] > p[i+1]: continue
    q = p[:i+1]
    q.sort()
    p = q + p[i+1:]
    index = 0
    for j in range(i+1):
        if p[j] < p[i+1]:
            index = j
    p[index], p[i+1] = p[i+1], p[index]
    break

p.reverse()
print(*p)