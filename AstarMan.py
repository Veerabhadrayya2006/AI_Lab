
import heapq

start = (2, 8, 3,
         1, 6, 4,
         7, 0, 5)
goal = (1, 2, 3,
        8, 0, 4,
        7, 6, 5)


def heuristic(state):
    distance = 0

    for i in range(9):
        tile = state[i]

        if tile != 0:
            current_row, current_col = divmod(i, 3)
            goal_index = goal.index(tile)
            goal_row, goal_col = divmod(goal_index, 3)

            distance += (
                abs(current_row - goal_row)
                + abs(current_col - goal_col)
            )

    return distance


def neighbors(state):
    zero = state.index(0)
    r, c = divmod(zero, 3)

    for dr, dc in [(-1, 0), (1, 0),
                   (0, -1), (0, 1)]:
        nr, nc = r + dr, c + dc

        if 0 <= nr < 3 and 0 <= nc < 3:
            j = nr * 3 + nc
            new_state = list(state)
            new_state[zero], new_state[j] = (
                new_state[j], new_state[zero]
            )
            yield tuple(new_state)


def astar(start, goal):
    pq = [(heuristic(start), 0, start)]
    parent = {start: None}
    cost = {start: 0}

    while pq:
        f, g, state = heapq.heappop(pq)

        if g != cost[state]:
            continue

        if state == goal:
            path = []
            while state is not None:
                path.append(state)
                state = parent[state]
            return path[::-1]

        for nxt in neighbors(state):
            new_g = g + 1

            if new_g < cost.get(nxt, float("inf")):
                cost[nxt] = new_g
                parent[nxt] = state
                h = heuristic(nxt)
                heapq.heappush(
                    pq, (new_g + h, new_g, nxt)
                )

    return None


path = astar(start, goal)

if path:
    for step, state in enumerate(path):
        h = heuristic(state)
        print(f"\nStep {step}: g={step}, h={h}, f={step+h}")
        for i in range(0, 9, 3):
            print(state[i:i+3])
else:
    print("No solution found")
