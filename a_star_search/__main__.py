import argparse

MAZE_1 = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 8, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 9, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],

]

MAZE_2 = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 9, 2, 2, 2, 2, 1], #1
    [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 2, 2, 2, 2, 2, 1], #2
    [1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 2, 2, 2, 3, 2, 2, 2, 2, 2, 2, 1], #3
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 2, 2, 3, 2, 2, 2, 2, 0, 0, 0, 1], #4
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 2, 2, 2, 3, 2, 2, 0, 0, 0, 0, 1], #5
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 2, 2, 3, 3, 0, 0, 0, 0, 0, 1], #6
    [1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 2, 2, 3, 3, 0, 0, 0, 0, 0, 1], #7
    [1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 3, 3, 3, 1, 0, 0, 0, 1], #8
    [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 3, 3, 3, 0, 0, 0, 0, 1], #9
    [1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 3, 3, 0, 1, 0, 0, 0, 1], #10
    [1, 0, 0, 1, 0, 8, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 3, 3, 0, 3, 3, 0, 0, 0, 1], #11
    [1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 3, 0, 3, 3, 0, 0, 0, 0, 1], #12
    [1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 3, 0, 0, 0, 0, 0, 1], #13
    [1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 3, 3, 3, 0, 0, 0, 0, 0, 1], #14
    [1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 3, 3, 0, 0, 0, 0, 0, 1], #15
    [1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 3, 3, 3, 0, 0, 0, 0, 0, 0, 1], #16
    [1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 3, 3, 3, 0, 0, 0, 0, 0, 0, 1], #17
    [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 3, 3, 0, 0, 0, 0, 0, 0, 0, 1], #18
    [1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 3, 3, 0, 0, 0, 0, 0, 0, 0, 0, 1], #19
    [1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 3, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], #20
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],

]

class colors:
    PURPLE = '\033[95m'
    RED       = '\033[31;1m'
    GREEN     = '\033[32;1m'
    YELLOW    = '\033[33;1m'
    BLUE      = '\033[34;1m'
    MAGENTA   = '\033[35;1m'
    CYAN      = '\033[36;1m'
    STEEL      = '\033[36;1m'
    ENDC      = '\033[0m'

MARK_MAP = {
    0: colors.GREEN + "#",
    1: colors.ENDC + "#",
    2: colors.YELLOW + "#",
    3: colors.BLUE + "#",
    6: colors.PURPLE + "*",
    7: colors.STEEL + "*",
    8: colors.RED + "S",
    9: colors.RED + "T",
}

COST = {
    0: 0,
    2: 4,
    3: 2,
    8: 0,
    9: 0,
}

def render_maze(maze):
    for i in range(len(maze)):
        for j in range(len(maze[i])):
            print(MARK_MAP[maze[i][j]], end=' ')
        print("\n", end="")


def astar_search(maze, start, end):
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
            return reconstruct_path(came_from, current)
        open_set.remove(current)
        for neighbor in get_neighbors(current):
            tentative_g_score = g_score[current] + COST[maze[neighbor[0]][neighbor[1]]]
            tentative_g_score = tentative_g_score + (2**0.5 if neighbor[0] != current[0] and neighbor[1] != current[1] else 1)
            if neighbor in g_score.keys() and tentative_g_score >= g_score[neighbor]:
                continue
            came_from[neighbor] = current
            g_score[neighbor] = tentative_g_score
            f_score[neighbor] = g_score[neighbor] + heuristic(neighbor, end)
            if neighbor not in open_set:
                open_set.append(neighbor)

def bidirectional_astar_search(maze, start, end):
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
            tentative_g_score_start = g_score_start[current_start] + COST[maze[neighbor_start[0]][neighbor_start[1]]]
            tentative_g_score_start = tentative_g_score_start + (2**0.5 if neighbor_start[0] != current_start[0] and neighbor_start[1] != current_start[1] else 1)
            if neighbor_start in g_score_start.keys() and tentative_g_score_start >= g_score_start[neighbor_start]:
                continue
            came_from_start[neighbor_start] = current_start
            g_score_start[neighbor_start] = tentative_g_score_start
            f_score_start[neighbor_start] = g_score_start[neighbor_start] + heuristic(neighbor_start, end)
            if neighbor_start not in open_set_start:
                open_set_start.append(neighbor_start)
        for neighbor_end in get_neighbors(current_end):
            tentative_g_score_end = g_score_end[current_end] + COST[maze[neighbor_end[0]][neighbor_end[1]]]
            tentative_g_score_end = tentative_g_score_end + (2**0.5 if neighbor_end[0] != current_end[0] and neighbor_end[1] != current_end[1] else 1)
            if neighbor_end in g_score_end.keys() and tentative_g_score_end >= g_score_end[neighbor_end]:
                continue
            came_from_end[neighbor_end] = current_end
            g_score_end[neighbor_end] = tentative_g_score_end
            f_score_end[neighbor_end] = g_score_end[neighbor_end] + heuristic(neighbor_end, start)
            if neighbor_end not in open_set_end:
                open_set_end.append(neighbor_end)
    return None



def run_algorithm(maze, method='uni', render=False):
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            if maze[i][j] == 8:
                start = (i, j)
            if maze[i][j] == 9:
                end = (i, j)
    if method == "uni":
        path = astar_search(maze, start, end)
        if render:
            for point in path:
                if point != end:
                    maze[point[0]][point[1]] = 6
            render_maze(maze)
    if method == "bi":
        path = bidirectional_astar_search(maze, start, end)
        if render:
            for point in path[0]:
                if point != end:
                    maze[point[0]][point[1]] = 6
            for point in path[1]:
                if point != start:
                    maze[point[0]][point[1]] = 7
            render_maze(maze)
        
        

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--maze", type=int, default=1, help="maze to use")
    parser.add_argument("--method", type=str, default="uni", help="method to use for path finding")
    args = parser.parse_args()

    mazes = [MAZE_1, MAZE_2]

    run_algorithm(mazes[args.maze - 1], method=args.method, render=True)
