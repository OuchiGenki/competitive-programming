import numpy as np

ax, ay = map(int, input().split())
bx, by = map(int, input().split())
cx, cy = map(int, input().split())
dx, dy = map(int, input().split())

def in_triangle(tri, pt):
    a = tri[0]
    b = tri[1]
    c = tri[2]
    p = pt

    ab = np.array([b[0] - a[0], b[1] - a[1], 0])
    bc = np.array([c[0] - b[0], c[1] - b[1], 0])
    ca = np.array([a[0] - c[0], a[1] - c[1], 0])
    ap = np.array([p[0] - a[0], p[1] - a[1], 0])
    bp = np.array([p[0] - b[0], p[1] - b[1], 0])
    cp = np.array([p[0] - c[0], p[1] - c[1], 0])

    cross_ab_ap = np.cross(ab, ap)[2]
    cross_bc_bp = np.cross(bc, bp)[2]
    cross_ca_cp = np.cross(ca, cp)[2]

    return cross_ab_ap > 0 and cross_bc_bp > 0 and cross_ca_cp > 0

flag = True
if in_triangle([(ax, ay), (bx, by), (cx, cy)], (dx, dy)):
    flag = False
if in_triangle([(bx, by), (cx, cy), (dx, dy)], (ax, ay)):
    flag = False
if in_triangle([(cx, cy), (dx, dy), (ax, ay)], (bx, by)):
    flag = False
if in_triangle([(dx, dy), (ax, ay), (bx, by)], (cx, cy)):
    flag = False

if flag:
    print('Yes')
else:
    print('No')