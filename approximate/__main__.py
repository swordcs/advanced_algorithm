import random
import argparse

def generate_data(data_num, set_num,inital_size=20, seed=0):
    random.seed(seed)

    X = {_ for _ in range(data_num)}
    choosen_data = set(random.sample(list(X), inital_size))
    subsets = {tuple(choosen_data)}

    while len(choosen_data) < len(X):
        subset_size = random.randint(1, inital_size)
        size1 = random.randint(1, subset_size)
        subset1 = set(random.sample(list(choosen_data), size1))
        subset2 = set(random.sample(list(X - choosen_data), min(subset_size - size1, len(X - choosen_data))))

        subsets.add(tuple(subset1 | subset2))
        choosen_data |= subset1 | subset2
        
    while len(subsets) < set_num:
        subset_size = random.randint(1, inital_size)
        subset = set(random.sample(list(X), subset_size))
        subsets.add(tuple(subset))

    assert choosen_data == X
    return tuple(subsets), tuple(X)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--num", type=int, default=1, help="number of data points")
    parser.add_argument("--method", type=str, default="greedy", help="method to use for set cover")
    parser.add_argument("--seed", type=int, default=0, help="random seed")
    args = parser.parse_args()


    subsets, all_data = generate_data(args.num, args.num, inital_size=20, seed=args.seed)
    if args.method == "greedy":
        from .greedy_version import set_cover_greedy
        C = set_cover_greedy(subsets, all_data)
    elif args.method == "lp":
        from .lp_version import set_cover_lp
        C = set_cover_lp(subsets, all_data)
    
    assert set(all_data) == {x for subset in C for x in subset}

    print("Number of Covered sets:", len(C))
    
