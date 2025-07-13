n, m = map(int, input().split())
a = [[] for i in range(m)]
set_list = []
for i in range(m):
    c = int(input())
    a = map(int, input().split())
    set_list.append(set(a))

res = 0
for i in range(2**m):
    #print("case : ", bin(i))
    check = set()
    for j in range(m):
        if ((i >> j) & 1):
            #print("add ", set_list[j])
            check |= set_list[j]
    #print(check)
    if len(check) == n:
        res += 1

print(res)