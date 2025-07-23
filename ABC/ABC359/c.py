sx, sy = map(int, input().split())
tx, ty = map(int, input().split())
ans = abs(ty - sy)
h = abs(ty - sy)

if (sx + sy) % 2 == 0:
    if tx <= sx:
        ans += max(0, (sx - h) - tx + 1) // 2
    else:
        ans += max(0, tx - (sx+1 + h) + 1) // 2
else:
    if tx <= sx:
        ans += max(0, (sx-1 - h) - tx + 1) // 2
    else:
        ans += max(0, tx - (sx + h) + 1) // 2

print(ans)