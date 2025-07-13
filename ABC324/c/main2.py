K = int(input())
S = set()

for i in range(2**10):
    tmp = ''
    for j in range(10):
        if i & (1 << j):
            tmp += str(9-j)
    if tmp != '':
        S.add(int(tmp))

print(sorted(list(S))[K])