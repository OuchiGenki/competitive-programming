s = input()
t = input()
if len(s) > len(t):
    print("No")
    exit()
flag = True
for i in range(len(s)):
    if s[i] != t[i]:
        flag = False
if flag:
    print("Yes")
else:
    print("No")