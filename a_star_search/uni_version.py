def astar_search(maze, start, end, cost):
    def heuristic(a, b):
        return abs(a[0] - b[0]) + abs(a[1] - b[1])

    def get_neighbors(point):
        neighbors = []
        for action in [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]:
            neighbor = (point[0] + action[0], point[1] + action[1])
            if neighbor[0] >= 0 and neighbor[1] >= 0 and maze[neighbor[0]][neighbor[1]] != 1:
                neighbors.append(neighbor)
        return neighbors

    def reconstruct_path(came_from, current):
        path = []
        while current in came_from:
            path.append(current)
            current = came_from[current]
        return path

    open_set = [start]
    came_from = {}
    g_score = {start: 0}
    f_score = {start: heuristic(start, end)}

    while open_set:
        current = min(open_set, key=lambda x: f_score[x])
        if current == end:
            print(g_score[current])
            return reconstruct_path(came_from, current)
        open_set.remove(current)
        for neighbor in get_neighbors(current):
            tentative_g_score = g_score[current] + cost[maze[neighbor[0]][neighbor[1]]]
            tentative_g_score = tentative_g_score + (2**0.5 if neighbor[0] != current[0] and neighbor[1] != current[1] else 1)
            if neighbor in g_score.keys() and tentative_g_score >= g_score[neighbor]:
                continue
            came_from[neighbor] = current
            g_score[neighbor] = tentative_g_score
            f_score[neighbor] = g_score[neighbor] + heuristic(neighbor, end)
            if neighbor not in open_set:
                open_set.append(neighbor)