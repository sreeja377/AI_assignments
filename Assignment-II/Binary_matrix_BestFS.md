```
import heapq
import math

# Directions: 8 possible moves
directions = [(-1, -1), (-1, 0), (-1, 1),
              (0, -1),          (0, 1),
              (1, -1),  (1, 0), (1, 1)]

def heuristic(x, y, n):
    # Euclidean distance to bottom-right
    return math.sqrt((n-1-x)**2 + (n-1-y)**2)

def best_first_search(grid):
    n = len(grid)
    if grid[0][0] != 0 or grid[n-1][n-1] != 0:
        return -1, []

    pq = []
    heapq.heappush(pq, (heuristic(0, 0, n), (0, 0), [(0, 0)]))
    visited = set()

    while pq:
        _, (x, y), path = heapq.heappop(pq)

        if (x, y) == (n-1, n-1):
            return len(path), path

        if (x, y) in visited:
            continue
        visited.add((x, y))

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n and grid[nx][ny] == 0 and (nx, ny) not in visited:
                new_path = path + [(nx, ny)]
                heapq.heappush(pq, (heuristic(nx, ny, n), (nx, ny), new_path))

    return -1, []

# Example usage
if __name__ == "__main__":
    grid = [[0, 0, 0],
            [1, 1, 0],
            [1, 1, 0]]

    length, path = best_first_search(grid)
    print(f"Best First Search → Path length: {length}, Path: {path}")

```
