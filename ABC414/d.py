import numpy as np

a = int(input())
n = int(input())
s = set()
for i in range(10**6+1):
    i = str(i)
    num1 = int(i[:-1] + i[::-1])
    num2 = int(i + i[::-1])
    print(i[:-1] + i[::-1],  i + i[::-1], len(i[:-1] + i[::-1]), len(i + i[::-1]))    
    if num1 <= n:
        s.add(num1)
    if num2 <= n:
        s.add(num2)

ans = set()
for i in range(10**6+1):
    i = str(np.base_repr(i, a))
    num1 = int(i[:-1] + i[::-1], a)
    num2 = int(i + i[::-1], a)
    #print(i[:-1] + i[::-1],  i + i[::-1], len(i[:-1] + i[::-1]), len(i + i[::-1]))