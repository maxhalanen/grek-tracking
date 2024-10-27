class Solution:
  def findLength(self, str1, k):

      map = {}

      unique = 0
      start = 0
      count = 0
      maxCount = 0

      for i in range(len(str1)):

        if str1[i] not in map:
          unique += 1
          map[str1[i]] = 1
        else:
          map[str1[i]] += 1
        count += 1

        while unique > k:
          if map[str1[start]] == 1:
            del map[str1[start]]
            unique -= 1
          else:
            map[str1[start]] -= 1
          start += 1
          count -= 1
        maxCount = max(count, maxCount)

      return maxCount
