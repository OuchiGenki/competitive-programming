N = int(input())
carpet = [['#' for i in range(3**N)] for j in range(3**N)]

def f(y, x, K):
    if K == 0:
        return
    
    for i in range(3**(K-1), 3**(K-1)*2):
        for j in range(3**(K-1), 3**(K-1)*2):
            carpet[y+i][x+j] = '.'
    
    for i in range(3):
        for j in range(3):
            f(y+3**(K-1)*i, x+3**(K-1)*j, K-1)

f(0, 0, N)

for row in carpet:
    print(''.join(row))