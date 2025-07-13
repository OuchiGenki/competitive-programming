s = input()
t = input()

flag = False
for i in range(len(s)):
    if i+len(t) > len(s): continue
    if s[i:i+len(t)] == t:
        flag = True

if flag: print("Yes")
else: print("No")