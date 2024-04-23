def bidirectional_astar_search(maze, start, end, cost):
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
    open_set_start = [start]
    open_set_end = [end]
    came_from_start = {}
    came_from_end = {}
    g_score_start = {start: 0}
    g_score_end = {end: 0}
    f_score_start = {start: heuristic(start, end)}
    f_score_end = {end: heuristic(end, start)}
    while open_set_start and open_set_end:
        current_start = min(open_set_start, key=lambda x: f_score_start[x])
        current_end = min(open_set_end, key=lambda x: f_score_end[x])
        
        if current_start in open_set_end or current_end in open_set_start:
            path_start = reconstruct_path(came_from_start, current_start if current_start in open_set_end else current_end)
            path_end = reconstruct_path(came_from_end, current_start if current_start in open_set_end else current_end)
            path_end.reverse()
            return path_start, path_end

        open_set_start.remove(current_start)
        open_set_end.remove(current_end)
        for neighbor_start in get_neighbors(current_start):
            tentative_g_score_start = g_score_start[current_start] + cost[maze[neighbor_start[0]][neighbor_start[1]]]
            tentative_g_score_start = tentative_g_score_start + (2**0.5 if neighbor_start[0] != current_start[0] and neighbor_start[1] != current_start[1] else 1)
            if neighbor_start in g_score_start.keys() and tentative_g_score_start >= g_score_start[neighbor_start]:
                continue
            came_from_start[neighbor_start] = current_start
            g_score_start[neighbor_start] = tentative_g_score_start
            f_score_start[neighbor_start] = g_score_start[neighbor_start] + heuristic(neighbor_start, end)
            if neighbor_start not in open_set_start:
                open_set_start.append(neighbor_start)
        for neighbor_end in get_neighbors(current_end):
            tentative_g_score_end = g_score_end[current_end] + cost[maze[neighbor_end[0]][neighbor_end[1]]]
            tentative_g_score_end = tentative_g_score_end + (2**0.5 if neighbor_end[0] != current_end[0] and neighbor_end[1] != current_end[1] else 1)
            if neighbor_end in g_score_end.keys() and tentative_g_score_end >= g_score_end[neighbor_end]:
                continue
            came_from_end[neighbor_end] = current_end
            g_score_end[neighbor_end] = tentative_g_score_end
            f_score_end[neighbor_end] = g_score_end[neighbor_end] + heuristic(neighbor_end, start)
            if neighbor_end not in open_set_end:
                open_set_end.append(neighbor_end)
    return None