from collections import deque

class Solution:
  def floodFill(self, matrix, x, y, newColor):
    
    if not matrix:
      return 0

    color = matrix[x][y]
    seen = set()
    rows, cols = len(matrix), len(matrix[0])
    
    def bfsFill(r, c):
      
      matrix[r][c] = newColor
      seen.add((r, c))
      deq = deque()
      deq.append((r, c))

      while deq:
        curr_r, curr_c = deq.popleft()

        for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
          nr, nc = curr_r + dr, curr_c + dc

          if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in seen and matrix[nr][nc] == color:
            matrix[nr][nc] = newColor
            seen.add((nr, nc))
            deq.append((nr, nc))

    bfsFill(x, y)

    return matrix
