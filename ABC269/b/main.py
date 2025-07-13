s = [input() for i in range(10)]
a = b = c = d = 0
flag1 = True
flag2 = True
for i in range(10):
    for j in range(10):
        if s[i][j]=='#' and flag1:
            a = i+1
            c = j+1
            flag1 = False
        if s[9-i][9-j]=='#' and flag2:
            b = 10-i
            d = 10-j
            flag2 = False

print(a, b)
print(c, d)