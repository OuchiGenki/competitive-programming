s = input()

cnt = 0
skip = False
for i in range(len(s)-1):
    if skip:
        skip = False
        continue
    if s[i:i+2] == "00":
        cnt+=1
        skip = True
print(len(s)-cnt)