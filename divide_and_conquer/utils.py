import random

def orientation(p, q, r):
    return (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])

def plot_points(points, hull, method):
    import matplotlib.pyplot as plt
    x, y = zip(*points)
    plt.scatter(x, y, color='black')
    for i in range(len(hull)):
        plt.scatter([hull[i][0]], [hull[i][1]], color='r')
    plt.savefig(f"./divide_and_conquer/share/{method}_{len(points)}points.png")
    plt.close()

def generat_points(num, seed=0):
    points = []
    random.seed(seed)
    for _ in range(num):
        x = random.random() * 100
        y = random.random() * 100
        points.append((x, y))
    return tuple(points)