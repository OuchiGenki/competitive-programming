import sys
sys.setrecursionlimit(10**8)
input = sys.stdin.readline

a, b = map(int, input().split())
if (a-1)//3 == (b-1)//3 and b-a == 1:
    print("Yes")
else:
    print("No")