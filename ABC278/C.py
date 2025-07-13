n, q = map(int, input().split())

dict = {}

for i in range(q):
    t, a, b = map(int, input().split())
    if t == 1:
        if a not in dict:
            dict[a] = set()
            dict[a].add(b)
        else:
            dict[a].add(b)
    
    elif t == 2:
        if a not in dict: continue
        dict[a].discard(b)
    
    elif t == 3:
        if a not in dict or b not in dict:
            print("No")
            continue
        if b not in dict[a] or a not in dict[b]:
            print("No")
            continue
        print("Yes")