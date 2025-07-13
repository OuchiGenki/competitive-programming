import sys
sys.setrecursionlimit(10**8)

k = int(input())

li = []
for i in range(1,2**10):
    num = ""
    for j in range(10, -1, -1):
        if (i>>j)&1:
            num += str(j)
    li.append(int(num))

li.sort()
print(li[k])