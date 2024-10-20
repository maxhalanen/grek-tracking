class Solution:
  def search(self, arr, target_sum):

    pointa = 0
    pointb = len(arr) - 1

    while pointa < pointb:

      if arr[pointa] + arr[pointb] < target_sum:
        pointa += 1
      elif arr[pointa] + arr[pointb] > target_sum:
        pointb -= 1
      else:
        return [pointa, pointb]

    # TODO: Write your code here
    return [-1, -1]
