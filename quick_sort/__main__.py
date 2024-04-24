import time
import random
import argparse
import matplotlib.pyplot as plt


def generate_data_sets(size, duplicates_percentage, sorted_most=True):
    data_set = [_ for _ in range(size)]
    data_set = data_set + random.sample(
        data_set,
        counts=[random.randint(0, size // 10) for _ in range(size)],
        k=int(size * duplicates_percentage),
    )
    data_set = data_set[-size:]
    if not sorted_most:
        random.shuffle(data_set)
    return tuple(data_set)


def quicksort(A, p, r):
    if p < r:
        q = partition(A, p, r)
        quicksort(A, p, q - 1)
        quicksort(A, q + 1, r)


def is_sorted(A):
    for i in range(len(A) - 1):
        if A[i] > A[i + 1]:
            return False
    return True

def qicksort_opt(A, p, r):
    if is_sorted(A):
        return
    if p < r:
        q = partition(A, p, r)
        quicksort(A, p, q - 1)
        quicksort(A, q + 1, r)

def partition(A, p, r):
    i = random.randint(p, r)
    A[r], A[i] = A[i], A[r]
    x = A[r]
    i = p - 1
    for j in range(p, r):
        if A[j] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i + 1], A[r] = A[r], A[i + 1]
    return i + 1


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--num", type=int, default=1, help="number of data points")
    parser.add_argument("--plot", action="store_true", help="plot the performance")
    parser.add_argument("--seed", type=int, default=0, help="random seed")

    args = parser.parse_args()

    random.seed(args.seed)

    time_cost = []
    time_cost_opt = []
    for i in range(11):
        data = generate_data_sets(args.num, 0.1 * i)
        start = time.time()
        quicksort(list(data), 0, len(data) - 1)
        time_cost.append(time.time() - start)

        start = time.time()
        qicksort_opt(list(data), 0, len(data) - 1)
        time_cost_opt.append(time.time() - start)


    
    plt.plot([0.1 * i for i in range(len(time_cost))], time_cost, label="origin")
    plt.plot([0.1 * i for i in range(len(time_cost_opt))], time_cost_opt, label="optimized")
    plt.legend()
    plt.xlabel("Duplicates Percentage")
    plt.ylabel("Time Cost")
    plt.title("Quick Sort Performance")
    plt.savefig(f"./quick_sort/share/{args.num}.jpg")
    