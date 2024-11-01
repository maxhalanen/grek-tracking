from collections import deque

class Solution:
  def maxAreaOfIsland(self, matrix):
    
    if not matrix:
      return 0

    maxSize = 0
    seen = set()
    rows, cols = len(matrix), len(matrix[0])
    
    def bfs(r, c):
      size = 1
      seen.add((r, c))
      deq = deque()
      deq.append((r, c))

      while deq:
        curr_r, curr_c = deq.popleft()

        for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
          nr, nc = curr_r + dr, curr_c + dc

          if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in seen and matrix[nr][nc] == 1:
            size += 1
            deq.append((nr, nc))
            seen.add((nr, nc))

      return size

    for r in range(rows):
      for c in range(cols):
        if matrix[r][c] == 1 and (r, c) not in seen:

          size = bfs(r, c)
          maxSize = max(size, maxSize)
    
    return maxSize
