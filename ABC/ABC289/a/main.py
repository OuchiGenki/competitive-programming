s = input()
ans = []
for i in s:
    if i=="0":
        ans.append('1')
    else:
        ans.append('0')
for i in ans:
    print(i, end="")
print()