from collections import deque

class Solution:
  def countClosedIslands(self, matrix):
    
    countClosedIslands = 0
    rows, cols = len(matrix), len(matrix[0])
    seen = set()
    isolated = False 

    def bfs(r, c):

      seen.add((r, c))
      deq = deque()
      deq.append((r, c))
      
      while deq: 
        curr_r, curr_c = deq.popleft()

        for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
          nr, nc = curr_r + dr, curr_c + dc
        
          if nr not in range(rows) or nc not in range(cols):
            return False

          if nr in range(rows) and nc in range(cols) and (nr, nc) not in seen and matrix[nr][nc] == 1:
            deq.append((nr, nc))
            seen.add((nr, nc))
      return True

    for r in range(rows):
      for c in range(cols):
        if matrix[r][c] == 1 and (r, c) not in seen:
          if bfs(r, c):
            countClosedIslands += 1

    return countClosedIslands
