s = input()
t = input()

if len(s) < len(t):
    print("UNRESTORABLE")
    exit()
ok = False
index = 0
for i in range(len(s)-len(t), -1, -1):
    cnt = 0
    for j in range(len(t)):
        if s[i+j] == t[j] or s[i+j] == '?':
            cnt += 1
    if cnt == len(t):
        index = i
        ok = True
        break
if ok == False:
    print("UNRESTORABLE")
    exit()

s = s[:index] + t + s[index+len(t):]
print(s.replace('?', 'a'))