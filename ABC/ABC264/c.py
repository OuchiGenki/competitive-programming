h1, w1 = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(h1)]
h2, w2 = map(int, input().split())
B = [list(map(int, input().split())) for _ in range(h2)]
for i in range(2**h1):
    for j in range(2**w1):
        flag = True
        y, x = [], []
        for k in range(h1):
            if i & (1 << k):
                y.append(k)
        for k in range(w1):
            if j & (1 << k):
                x.append(k)
        if len(y) != h2 or len(x) != w2:
            continue

        for r in range(h2):
            for c in range(w2):
                if A[y[r]][x[c]] != B[r][c]:
                    flag = False
                    break
            if not flag:
                break
        
        if flag:
            print('Yes')
            exit()
    
print('No')