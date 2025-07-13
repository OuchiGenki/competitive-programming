import sys
import networkx as nx
import matplotlib.pyplot as plt
sys.setrecursionlimit(10**8)

N = int(input())

G = nx.cycle_graph(2*N)
pos = nx.circular_layout(G)
for i in range(N):
    a,b = map(int, input().split())
    G.add_edge(a-1,b-1)

if nx.is_planar(G):
    print("No")
else:
    print("Yes")
print(nx.is_simple_path(G))
print(nx.planar_layout(G))
nx.draw_networkx(G)
plt.show()