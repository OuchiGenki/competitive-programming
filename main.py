from itertools import product

def check(v):
    flag = True
    if not (v[0] <= v[1] <= v[2]):
        flag = False
    if not (v[3] <= v[4]):
        flag = False
    if not (v[0] <= v[3] <= v[5]):
        flag = False
    if not (v[1] <= v[4]):
        flag = False
    return flag        


def show(v):
    v = list(map(str, v))
    idx = 0
    print('-'*5)
    for l in [3, 2, 1]:
        print('|'.join(v[idx:idx+l]))
        print('-'*l)
        idx += l
    print()


cnt = 0
for v in product([1, 2, 3], repeat=6):
    if check(v):
        show(v)
        print()
        cnt += 1
print(cnt)