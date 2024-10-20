import math

class Solution:
  def mySqrt(self, x: int) -> int:
    # TODO: Write your code here

    if x == 0:
      return 0
    
    if x == 1:
      return 1 

    left = 0
    right = x // 2

    while left <= right:

      mid = left + (right - left) // 2

      square = mid * mid

      if square > x:
        right = mid - 1
      elif square < x:
        left = mid + 1
      else:
        return mid


    else:
      return right

    return 0
