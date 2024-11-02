class Solution:
  def findLength(self, str1, k):
     
    map = {}
    start =  0
    maxCount = 0
    mapMax = 0
    
    for end in range(len(str1)):

      char = str1[end]

      if char not in map:
        map[char] = 0
      map[char] += 1

      mapMax = max(mapMax, map[char])

      while (end - start + 1) - mapMax > k:

        map[str1[start]] -= 1
        if map[str1[start]] == 0:
          del map[str1[start]]

        start += 1

      maxCount = max(end - start + 1, maxCount)
    
    return maxCount
