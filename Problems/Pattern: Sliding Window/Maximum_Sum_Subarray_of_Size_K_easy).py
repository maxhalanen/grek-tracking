import math
class Solution:
  def findMaxSumSubArray(self,k, arr):

    maxSum = 0
    
    print(maxSum)
    
    for i in range(len(arr) - k + 1):
      newSum = 0
     

      for j in range(k):
        
        newSum += arr[i+j]
      
      maxSum = max(newSum, maxSum)

    return maxSum
    
