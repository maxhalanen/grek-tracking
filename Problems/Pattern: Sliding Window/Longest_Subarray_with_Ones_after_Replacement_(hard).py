import math

class Solution:
    def findLength(self, arr, k):
      
      start = 0

      for end in range(len(arr)):
        
        if arr[end] == 0:
          k -= 1
        
        if k < 0:
          
          if arr[start] == 0:
            k += 1
          start += 1
      
      return end - start + 1
