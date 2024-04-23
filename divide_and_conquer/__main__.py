import time
import random
import argparse

from .enumerate_version import convex_hull_enum
from .graham_version import convex_hull_graham
from .divide_version import convex_hull_divide

def generat_points(num, seed=0):
    points = []
    random.seed(seed)
    for _ in range(num):
        x = random.random() * 100
        y = random.random() * 100
        points.append((x, y))
    return tuple(points)

ALGORITHM = {
    "enum": convex_hull_enum,
    "graham": convex_hull_graham,
    "divide": convex_hull_divide

}

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--num", type=int, default=2000, help="number of points to generate")
    parser.add_argument("--method", type=str, default="all", help="method to use for convex hull computation")
    parser.add_argument("--plot", action="store_true", help="plot the points and the convex hull")
    parser.add_argument("--seed", type=int, default=0, help="seed for random number generation")
    parser.add_argument("--profile", action="store_true", help="profile the code")
    args = parser.parse_args()
    points = generat_points(args.num)
    result = {}
    if args.method not in ALGORITHM and args.method != "all":
        print(f"Invalid method {args.method}")
        return

    cost_stats = {}
    if args.method == "all":
        alg_run = ALGORITHM
    else:
        alg_run = [args.method]

    for method in alg_run.keys():
        res = run_algorithm(method, points)
        result[method] = res['hull']
        cost_stats[method] = res['time']

    if args.plot:
        for method, hull in result.items():
            plot_points(points, hull, method)
    if args.profile:
        for method, cost in cost_stats.items():
            print(f"Point: {args.num}, Method: {method}, Time: {cost}")


def run_algorithm(method, points):
    start_time = time.time()  
    res = ALGORITHM[method](points=points)
    end_time  = time.time()
    return {'hull': res, 'time': end_time - start_time}

def plot_points(points, hull, method):
    import matplotlib.pyplot as plt
    x, y = zip(*points)
    plt.scatter(x, y, color='black')
    for i in range(len(hull)):
        plt.scatter([hull[i][0]], [hull[i][1]], color='r')
    plt.savefig(f"./divide_and_conquer/share/{method}_{len(points)}points.png")
    plt.close()

if __name__ == "__main__":
    main()