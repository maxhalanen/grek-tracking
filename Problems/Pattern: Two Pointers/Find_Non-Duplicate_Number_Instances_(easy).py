class Solution:
  def moveElements(self, arr):
    # TODO: Write your code here
    
    pointa = 0
    pointb = 1

    count = 1

    while pointa < len(arr) and pointb < len(arr):

      if arr[pointa] == arr[pointb]:
        pointb += 1
      else:
        count += 1
        pointa = pointb
        pointb += 1

    return count
