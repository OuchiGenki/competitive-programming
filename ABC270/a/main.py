a, b = map(int, input().split())
ans = 0

if a-4 >= 0 or b-4 >= 0:
    ans += 4
    if a-4 >= 0:
        a-=4
    if b-4 >= 0:
        b-=4

if a-2 >= 0 or b-2 >= 0:
    ans += 2
    if a-2 >= 0:
        a-=2
    if b-2 >= 0:
        b-=2

if a-1 >= 0 or b-1 >= 0:
    ans += 1
    if a-1 >= 0:
        a-=1
    if b-1 >= 0:
        b-=1

print(ans)