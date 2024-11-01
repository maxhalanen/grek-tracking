from collections import deque

class Solution:
  def findIslandPerimeter(self, matrix):

    seen = set()
    rows, cols = len(matrix), len(matrix[0])

    def bfsCount(r, c):
       
      count = 0

      seen.add((r, c))
      deq = deque()
      deq.append((r, c))
    
      while deq:
        curr_r, curr_c = deq.popleft()

        for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
          nr, nc = curr_r + dr, curr_c + dc

          if nr < 0 or nr >= rows or nc < 0 or nc >= cols:
              count += 1
          elif matrix[nr][nc] == 0:
              count += 1
              
          if nr in range(rows) and nc in range(cols) and matrix[nr][nc] == 1 and (nr, nc) not in seen:
            deq.append((nr, nc))
            seen.add((nr, nc))

      print(count)
      return count
        

    for r in range(rows):
      for c in range(cols):
        if (r, c) not in seen and matrix[r][c] == 1:
          return bfsCount(r, c)

    return 0
    
