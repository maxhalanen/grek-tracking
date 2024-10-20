class Solution:
  def searchTriplets(self, arr, target):
    count = 0

    arr.sort()

    for i in range(len(arr) - 2):
      
      a = i + 1
      b = a + 1

      while a < len(arr) - 1:

        if b >= len(arr):
          a += 1
          b = a + 1    
          continue
      
        currSum = arr[i] + arr[a] + arr[b]

        if currSum < target:
          count += 1
          b += 1
        elif currSum >= target:
          b += 1
        else:
          count += 1
          b += 1

    return count
