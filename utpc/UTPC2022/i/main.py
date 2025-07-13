import sys
import random
import copy
from random import randint, randrange
sys.setrecursionlimit(10**8)
input = sys.stdin.readline

n = list("5020")
ok = 0
for i in range(1000000):
    tmp = copy.deepcopy(n)
    #tmp[0] = randint(0, 9)
    tmp[1] = randint(0, 9)
    tmp[2] = randint(0, 9)
    tmp[3] = randint(0, 9)
    n1 = int("".join(map(str, n)))
    n2 = int("".join(map(str, tmp)))
    if n1 < n2:
        ok += 1

print(ok/1000000*100, "%")