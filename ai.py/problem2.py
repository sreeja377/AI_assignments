from collections import deque
people = {'A':5, 'M':10, 'GM':20, 'GF':25}
initial_state = (frozenset(['A','M','GM','GF']), frozenset(), 0, 'L')
goal_state = frozenset()

def bfs():
    queue = deque()
    queue.append( (initial_state, []) )
    visited = set()
    visited.add(initial_state)
    
    while queue:
        (left, right, time, umbrella), path = queue.popleft()
        
        
        if left == goal_state and time <= 60:
            return path + [ (left, right, time, umbrella) ]
        
        if umbrella == 'L':
            
            for p1 in left:
                for p2 in left:
                    if p1 < p2: 
                        new_left = set(left)
                        new_left.remove(p1)
                        new_left.remove(p2)
                        new_right = set(right)
                        new_right.add(p1)
                        new_right.add(p2)
                        cross_time = max(people[p1], people[p2])
                        new_state = (frozenset(new_left), frozenset(new_right), time + cross_time, 'R')
                        if new_state not in visited and new_state[2] <= 60:
                            queue.append( (new_state, path + [(left, right, time, umbrella)]) )
                            visited.add(new_state)
        else:
            
            for p in right:
                new_left = set(left)
                new_left.add(p)
                new_right = set(right)
                new_right.remove(p)
                cross_time = people[p]
                new_state = (frozenset(new_left), frozenset(new_right), time + cross_time, 'L')
                if new_state not in visited and new_state[2] <= 60:
                    queue.append( (new_state, path + [(left, right, time, umbrella)]) )
                    visited.add(new_state)
    return None

solution = bfs()


if solution:
    for step in solution:
        left, right, time, umbrella = step
        print(f"Left: {left}, Right: {right}, Time: {time}, Umbrella: {umbrella}")
    
    left, right, time, umbrella = solution[-1]
    print(f"Left: {left}, Right: {right}, Time: {time}, Umbrella: {umbrella}")
else:
    print("No solution found within 60 minutes.")

