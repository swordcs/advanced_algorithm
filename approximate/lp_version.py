from pulp import LpProblem, LpVariable, lpSum, LpMinimize, value


def set_cover_lp(subsets, all_data):
    U = set(all_data)
    F = subsets
    C = set()
    prob = LpProblem("Set Cover", LpMinimize)
    x = {i: LpVariable("x{}".format(i), 0, 1, 'Binary') for i in range(len(F))}
    prob += lpSum(x.values())
    for e in U:
        prob += lpSum(x[i] for i in range(len(F)) if e in F[i]) >= 1
    prob.solve()
    for i in range(len(F)):
        if value(x[i]) == 1:
            C.add(F[i])
    return C