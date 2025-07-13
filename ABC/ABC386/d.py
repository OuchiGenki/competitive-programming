N, M = map(int, input().split())
XYC = []
for i in range(M):
    x, y, c = input().split()
    XYC.append((int(x), int(y), c))
XYC.sort()
min_y = float('inf')
ans = 'Yes'
for x, y, c in XYC:
    if c == 'B':
        if y >= min_y:
            ans = 'No'
    else:
        min_y = min(min_y, y)
print(ans)