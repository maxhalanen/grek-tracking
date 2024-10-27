import math

class Solution:
  def findLength(self, fruits):
      max_length = 0
      length = 0
      map = {}
      start = 0
      fruitCount = 0
      for i in range(len(fruits)):
        
        if fruits[i] not in map:
          map[fruits[i]] = 1
          fruitCount += 1
        else:
          map[fruits[i]] += 1
        length += 1
        while fruitCount > 2:
          if map[fruits[start]] == 1:
            del map[fruits[start]]
            fruitCount -= 1
          else:
            map[fruits[start]] -= 1
          start += 1
          length -= 1
        
        max_length = max(max_length, length)
          
      # TODO: Write your code here
      return max_length
