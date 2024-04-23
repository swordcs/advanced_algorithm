import random

def generate_data(data_num, set_num,inital_size=20, seed=0):
    random.seed(seed)

    X = {_ for _ in range(data_num)}
    choosen_data = set(random.sample(list(X), inital_size))
    subsets = {tuple(choosen_data)}

    while len(choosen_data) < len(X):
        subset_size = random.randint(1, inital_size)
        size1 = random.randint(1, subset_size)
        subset1 = set(random.sample(list(choosen_data), size1))
        subset2 = set(random.sample(list(X - choosen_data), max(subset_size - size1, len(X - choosen_data))))

        subsets.add(tuple(subset1 | subset2))
        choosen_data |= subset1 | subset2
        
    while len(subsets) < set_num:
        subset_size = random.randint(1, inital_size)
        subset = set(random.sample(list(X), subset_size))
        subsets.add(tuple(subset))

    assert choosen_data == X
    return subsets, X


if __name__ == "__main__":
    
    subsets, all_data = generate_data(1000, 1000, inital_size=20, seed=random.randint(0, 1000))
