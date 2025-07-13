N = int(input())
if N == 1:
    print(0)
    exit()
N -= 1

d = 1
while 9 * 10 ** ((d+1)//2 - 1) < N:
    N -= 9 * 10 ** ((d+1)//2 - 1)
    d += 1
S = str(10 ** ((d+1)//2 - 1) + N - 1)

if d % 2 == 0:
    print(S + S[::-1])
else:
    print(S[:-1] + S[::-1])