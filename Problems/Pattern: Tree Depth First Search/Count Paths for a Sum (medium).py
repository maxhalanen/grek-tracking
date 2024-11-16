#class TreeNode:
#  def __init__(self, val, left=None, right=None):
#    self.val = val
#    self.left = left
#    self.right = right

class Solution:
  def countPaths(self, root, S):

    count = [0]

    def recurse(sum, root, arr):

      if not root:
        return 0

      arr.append(root.val)

      pathCount, pathSum = 0,0

      for i in range(len(arr) -1, -1, -1):
        pathSum += arr[i]

        if pathSum == sum:
          count[0] += 1 

      recurse(sum, root.left,  arr)

      recurse(sum, root.right, arr)

      del arr[-1]

      return pathCount

    recurse(S, root, [])

    return count[0] 
  

