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

def a_star_search(grid):
    n = len(grid)
    if grid[0][0] != 0 or grid[n-1][n-1] != 0:
        return -1, []

    pq = []
    heapq.heappush(pq, (heuristic(0, 0, n), 0, (0, 0), [(0, 0)]))
    visited = {}

    while pq:
        f, g, (x, y), path = heapq.heappop(pq)

        if (x, y) == (n-1, n-1):
            return len(path), path

        if (x, y) in visited and visited[(x, y)] <= g:
            continue
        visited[(x, y)] = g

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n and grid[nx][ny] == 0:
                new_g = g + 1
                new_f = new_g + heuristic(nx, ny, n)
                new_path = path + [(nx, ny)]
                heapq.heappush(pq, (new_f, new_g, (nx, ny), new_path))

    return -1, []

# Example usage
if __name__ == "__main__":
    grid = [[0, 0, 0],
            [1, 1, 0],
            [1, 1, 0]]

    length, path = a_star_search(grid)
    print(f"A* Search → Path length: {length}, Path: {path}")

```
