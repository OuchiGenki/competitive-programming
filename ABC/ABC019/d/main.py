import sys

n = int(input())
max_d = 0
edge = 1
for i in range(n):
    print("? 1 {0}".format(i+1))
    sys.stdout.flush()
    d = int(input())
    if max_d < d:
        max_d = d
        edge = i+1

max_d = 0
for i in range(n):
    print("? {0} {1}".format(edge, i+1))
    sys.stdout.flush()
    d = int(input())
    max_d = max(max_d, d)

print("!", max_d)