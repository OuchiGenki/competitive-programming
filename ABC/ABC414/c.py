import numpy as np

a = int(input())
n = int(input())
s = set()
for i in range(10**6+1):
    i = str(i)
    num1 = int(i[:-1] + i[::-1])
    num2 = int(i + i[::-1])
    if num1 <= n:
        s.add(num1)
    if num2 <= n:
        s.add(num2)

ans = set()
for x in list(s):
    x = str(np.base_repr(x, a))
    d = len(x)
    flag = True
    for i in range(d):
        if x[i] != x[d-1-i]:
            flag = False
            break
    if flag:
        ans.add(int(x, a))

print(sum(ans))