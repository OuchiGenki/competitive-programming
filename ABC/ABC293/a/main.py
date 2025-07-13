s = list(input())
for i in range(0, len(s)//2):
    s[2*i], s[2*i+1] = s[2*i+1], s[2*i]
print(*s, sep="")