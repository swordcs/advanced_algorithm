from .utils import orientation


def convex_hull_divide(points):
    sorted_points = sorted(points, key=lambda p: p[0])
    return convex_hull_recursive(sorted_points)


def convex_hull_recursive(points):
    if len(points) <= 3:
        return points
    mid = len(points) // 2
    left_hull = convex_hull_recursive(points[:mid])
    right_hull = convex_hull_recursive(points[mid:])
    return merge_hulls(left_hull, right_hull)


def merge_hulls(left_hull, right_hull):
    lt = left_hull[-1]
    lb = left_hull[0]
    rt = right_hull[-1]
    rb = right_hull[0]
    while True:
        olt, olb, ort, orb = lt, lb, rt, rb
        for rp in right_hull:
            if orientation(lt, rt, rp) > 0:
                rt = rp
            if orientation(lb, rb, rp) < 0:
                rb = rp
        for lp in left_hull:
            if orientation(rt, lt, lp) < 0:
                lt = lp
            if orientation(rb, lb, lp) > 0:
                lb = lp
        if (olt, olb) == (lt, lb) and (ort, orb) == (rt, rb):
            break
    hull = []
    for p in left_hull:
        if orientation(lb, lt, p) >= 0:
            hull.append(p)
    for p in right_hull:
        if orientation(rb, rt, p) <= 0:
            hull.append(p)
    return hull
