N = int(input())
left = 1
right = N
while right-left > 1:
    mid = (left + right) // 2
    print('?', mid, flush=True)
    res = int(input())
    if res == 0:
        left = mid
    else:
        right = mid
print('!', left)