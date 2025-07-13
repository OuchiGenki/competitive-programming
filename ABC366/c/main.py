Q = int(input())
d = dict()
answer = []
num = 0
for i in range(Q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        x = query[1]
        if x not in d:
            d[x] = 1
            num += 1
        else:
            d[x] += 1
            if d[x] == 1:
                num += 1

    elif query[0] == 2:
        x = query[1]
        d[x] -= 1
        if d[x] == 0:
            num -= 1

    elif query[0] == 3:
        answer.append(num)
    
for i in answer:
    print(i)
