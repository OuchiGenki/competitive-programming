n = int(input())
ans = []
ans.append(format(n//16, 'x'))
ans.append(format(n%16, 'x'))
for i in ans:
    print(i.upper(), end="")
print()