s = input()
ans = 0
for i in range(len(s)):
    sum = 0
    for j in range(i, len(s)):
        if s[j] in ['A', 'C', 'G', 'T']:
            sum += 1
        else:
            break
    ans = max(ans, sum)
print(ans)