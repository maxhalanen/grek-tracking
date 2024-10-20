import math

class Solution:
  def findMinSubArray(self, s, arr):

    mink = math.inf
    
    for i in range(len(arr)):

      sum = 0
      k = 0

      while sum < s and (i + k) < len(arr):
        sum += arr[i + k]
        k += 1
        if k < mink and sum >= s:
          mink = k
    
    if mink == math.inf:
      return 0 

    return mink
         
