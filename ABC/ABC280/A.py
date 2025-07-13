h, w = map(int, input().split())
ans = 0
for i in range(h):
    str = input()
    for j in range(w):
        if str[j] == "#":
            ans += 1
print(ans)