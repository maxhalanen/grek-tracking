from collections import deque

class Solution:

  def countIslands(self, matrix):
    
    totalIslands = 0
    seen = set()
    rows, cols = len(matrix), len(matrix[0])

    def bfs(r, c):

      seen.add((r, c))
      deq = deque()
      deq.append((r, c))
      
      while deq: 
        curr_r, curr_c = deq.popleft()

        for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
          nr, nc = curr_r + dr, curr_c + dc
        
          if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in seen and matrix[nr][nc] == 1:
            deq.append((nr, nc))
            seen.add((nr, nc))
    
    for r in range(rows):
      for c in range(cols):
        if (r, c) not in seen and matrix[r][c] == 1:
          bfs(r,c)
          totalIslands += 1

    return totalIslands
