import heapq

GOAL = (1,2,3,4,5,6,7,8,0)
MOVES = {'up': -3, 'down': 3, 'left': -1, 'right': 1}

def manhattan(state):
    return sum(abs((val-1)//3 - i//3) + abs((val-1)%3 - i%3)
               for i, val in enumerate(state) if val)

def get_neighbors(state):
    i = state.index(0)
    neighbors = []
    for move, d in MOVES.items():
        j = i + d
        if 0 <= j < 9 and not (move == 'left' and i % 3 == 0) and not (move == 'right' and i % 3 == 2):
            lst = list(state)
            lst[i], lst[j] = lst[j], lst[i]
            neighbors.append(tuple(lst))
    return neighbors

def astar(start):
    heap = [(manhattan(start), 0, start, [])]
    visited = set()
    while heap:
        f, g, state, path = heapq.heappop(heap)
        if state == GOAL:
            return path + [state]
        if state in visited: continue
        visited.add(state)
        for neighbor in get_neighbors(state):
            heapq.heappush(heap, (g+1+manhattan(neighbor), g+1, neighbor, path + [state]))
    return None

start = (1,2,3,4,0,6,7,5,8)
path = astar(start)
for p in path:
    print(p[:3], p[3:6], p[6:], sep="\n")
    print("---")