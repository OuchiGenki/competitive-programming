import math

t = int(input())
l, X, Y = map(int, input().split())
q = int(input())

for i in range(q):
    e = int(input())
    y = -(l/2)*math.sin(2*math.pi*(e/t))
    z = -(l/2)*math.cos(2*math.pi*(e/t)) + l/2
    w = math.sqrt(X**2+(Y-y)**2)
    print(math.degrees(math.atan(z/w)))