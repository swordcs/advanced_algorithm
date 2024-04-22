def convex_hull_enum(points):
    hull = []
    mask = [True] * len(points)
    length = len(points)
    for i in range(3, length):
        for j in range(2, i):
            for k in range(1, j):
                for l in range(0, k):
                    res = which_in_convex_hull(points, [i, j, k, l])
                    if res >= 0:
                        mask[res] = False  
                        
    for i in range(length):
        if mask[i]:
            hull.append(points[i])
    return tuple(hull)

def which_in_convex_hull(points, indices):
    i, j, k, l = indices
    if in_triangle(points[i], points[j], points[k], points[l]):
        return l
    if in_triangle(points[i], points[j], points[l], points[k]):
        return k
    if in_triangle(points[i], points[k], points[l], points[j]):
        return j
    if in_triangle(points[j], points[k], points[l], points[i]):
        return i
    return -1

def in_triangle(p1, p2, p3, p):
    return (p1[0] - p[0]) * (p2[1] - p[1]) - (p2[0] - p[0]) * (p1[1] - p[1]) >= 0 and \
           (p2[0] - p[0]) * (p3[1] - p[1]) - (p3[0] - p[0]) * (p2[1] - p[1]) >= 0 and \
           (p3[0] - p[0]) * (p1[1] - p[1]) - (p1[0] - p[0]) * (p3[1] - p[1]) >= 0