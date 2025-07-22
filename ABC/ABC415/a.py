n = int(input())
A = set(list(map(int, input().split())))
x = int(input())
if x in A:
    print("Yes")
else:
    print("No")