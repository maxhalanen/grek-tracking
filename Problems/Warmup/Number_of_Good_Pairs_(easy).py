class Solution:
  def numGoodPairs(self, nums):
    pairCount = 0

    map = {}

    for i in nums:
      
      map[i] = map.get(i, 0) + 1

      pairCount += map[i] - 1
    
    # TODO: Write your code here
    return pairCount
