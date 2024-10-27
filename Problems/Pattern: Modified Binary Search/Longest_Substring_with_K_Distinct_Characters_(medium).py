# This file should be in sliding window 

class Solution:
  def findLength(self, str1, k):

      chars = {}
      start = 0
      count = 0
      maxCount = 0
      arr = list(str1)
      
      for i in range(len(str1)):

        if arr[i] in chars:
          chars[arr[i]] += 1
        else:
          chars[arr[i]] = 1
        
        count += 1

        if len(chars) > k:
          while len(chars) > k:

            chars[arr[start]] -= 1
            count -= 1
            if chars[arr[start]] == 0:
              chars.pop(arr[start])    
            start += 1
        print(count)
        maxCount = max(count, maxCount)          

      # TODO: Write your code here
      return maxCount


