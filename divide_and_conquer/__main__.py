import time
import argparse

from .utils import generat_points, plot_points
from .enumerate_version import convex_hull_enum
from .graham_version import convex_hull_graham
from .divide_version import convex_hull_divide



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
    result = {}
    points = generat_points(args.num)
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



if __name__ == "__main__":
    main()