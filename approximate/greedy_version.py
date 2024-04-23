def set_cover_greedy(subsets, all_data):
    U = set(all_data)
    F = subsets
    C = set()
    while U:
        S = max(F, key=lambda S: len(set(S)& U))
        C.add(S)
        U -= set(S)
    return C