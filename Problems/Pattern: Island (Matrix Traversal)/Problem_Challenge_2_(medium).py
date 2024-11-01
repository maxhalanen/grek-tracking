from collections import deque

class Solution:
  def findDistinctIslandsDFS(self, matrix):
    
    seen = set()
    rows, cols = len(matrix), len(matrix[0])
    shapes = set()

    def bfs(r, c):
      
      seen.add((r, c))
      deq = deque()
      deq.append((r, c))
      stringDir = ""

      while deq:
        curr_r, curr_c = deq.popleft()

        for dr, dc, direction in [(1, 0, "D"), (-1, 0, "U"), (0, 1, "R"), (0, -1, "L")]:
          nr, nc = curr_r + dr, curr_c + dc
          
          if nr in range(rows) and nc in range(cols) and matrix[nr][nc] == 1 and (nr, nc) not in seen:
            seen.add((nr, nc))
            deq.append((nr, nc))
            stringDir += direction
            
      shapes.add(stringDir)

    for r in range(rows):
      for c in range(cols):
        if (r, c) not in seen and matrix[r][c] == 1:
          bfs(r, c)

    return len(shapes)
