import sys
sys.setrecursionlimit(10**8)

s = input()

flag = True
for i in range(16):
    if i%2==0:
        continue
    if s[i]!="0":
        flag = False

if flag:
    print("Yes")
else:
    print("No")