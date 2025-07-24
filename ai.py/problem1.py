from collections import deque
def is_goal(state):
    return state == ('W', 'W', 'W', '_', 'E', 'E', 'E')

def get_next_states(state):
    next_states = []
    empty_index = state.index('_')

    for move in [-2, -1, 1, 2]:
        new_index = empty_index + move
        if 0 <= new_index < len(state):
          if abs(move) == 1:
                if (state[new_index] == 'E' and move == -1) or (state[new_index] == 'W' and move == 1):
                    continue
                new_state = list(state)
                new_state[empty_index], new_state[new_index] = new_state[new_index], new_state[empty_index]
                next_states.append(tuple(new_state))
            elif abs(move) == 2:
                middle_index = empty_index + (move // 2)
                
                if (state[middle_index] == 'E' and move == -2) or (state[middle_index] == 'W' and move == 2):
                    new_state = list(state)
                    new_state[empty_index], new_state[new_index] = new_state[new_index], new_state[empty_index]
                    next_states.append(tuple(new_state))
    return next_states

def bfs(start):
    queue = deque()
    queue.append((start, [start]))
    visited = set()
    visited.add(start)

    while queue:
        current, path = queue.popleft()
        if is_goal(current):
            return path

        for next_state in get_next_states(current):
            if next_state not in visited:
                visited.add(next_state)
                queue.append((next_state, path + [next_state]))

    return None

start_state = ('E', 'E', 'E', '_', 'W', 'W', 'W')
solution_path = bfs(start_state)

if solution_path:
    print("Solution found! The path is:\n")
    for step in solution_path:
        print(step)
else:
    print("No solution found.")

