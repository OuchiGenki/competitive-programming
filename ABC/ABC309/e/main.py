import sys
sys.setrecursionlimit(10**8)
input = sys.stdin.readline

n, m = map(int, input().split())
g = [[] for i in range(n)]