s = input()
ans = []
for i in range(len(s)):
    if s[i] == '#':
        ans.append(str(i+1))
for i in range(0, len(ans), 2):
    print(ans[i]+','+ans[i+1])