from .utils import orientation


def convex_hull_graham(points):
    # Sort the points based on their polar angle with respect to the lowest point
    lowest_point = min(points, key=lambda p: p[1])

    sorted_points = sorted(
        [_ for _ in points if _ != lowest_point],
        key=lambda p: -(p[0] - lowest_point[0])
        / (((p[0] - lowest_point[0]) ** 2 + (p[1] - lowest_point[1]) ** 2) ** 0.5),
    )
    stack = [lowest_point, sorted_points[0]]
    for i in range(1, len(sorted_points)):
        while (
            len(stack) > 1 and orientation(stack[-2], stack[-1], sorted_points[i]) >= 0
        ):
            stack.pop()
        stack.append(sorted_points[i])
    return tuple(stack)



