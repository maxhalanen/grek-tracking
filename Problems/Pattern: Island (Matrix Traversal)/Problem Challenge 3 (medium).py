from collections import deque

class Solution:
  def hasCycle(self, matrix):
    
    rows, cols = len(matrix), len(matrix[0])
    seen = set()

    def cycleHit(r, c, prevR, prevC, startChar):

      if r not in range(rows) or c not in range(cols) or matrix[r][c] != startChar:
        return False

      if (r,c) in seen:
        return True

      seen.add((r, c))

      for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        newR, newC = r + dr, c + dc
        if newR != prevR or newC != prevC:
          if cycleHit(newR, newC, r, c, startChar):
            return True
      return False


    for r in range(rows):
      for c in range(cols):
        if (r,c) not in seen:

          if cycleHit(r,  c, -1, -1, matrix[r][c]):
            return True

    return False
