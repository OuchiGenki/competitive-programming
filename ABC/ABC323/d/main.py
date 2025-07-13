import sys, copy
sys.setrecursionlimit(10**8)

n = int(input())
s = []
c = []
d = dict()
check_list = set()
next_check_list = set()

ans = 0

for i in range(n):
    S, C = map(int, input().split())
    s.append(S)
    check_list.add(S)
    d[S] = C
    ans += C

s.sort()

while len(check_list):
    for i in sorted(list(check_list)):
        #print(check_list)
        dn = d[i]//2
        ans -= dn*2
        ans += dn
        d[i] = d[i]%2

        if dn!=0:
            next_check_list.add(2*i)
            #print("yeah")

            if 2*i in d:
                #print("add key1=", 2*i, end=" ")
                d[2*i] += dn
                #print("res=", d[2*i])
            else:
                #print("add key2=", 2*i, end=" ")
                d[2*i] = dn
                #print("res=", d[2*i])
    check_list = copy.deepcopy(next_check_list)
    next_check_list = set()

print(ans)