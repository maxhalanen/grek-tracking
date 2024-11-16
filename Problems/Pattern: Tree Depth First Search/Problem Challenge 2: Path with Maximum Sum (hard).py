import math

#class TreeNode:
#  def __init__(self, val, left=None, right=None):
#    self.val = val
#    self.left = left
#    self.right = right


class Solution:

  def findMaximumPathSum(self, root):
    
    self.globalMaximumSum = -math.inf

    def recurse(root):
      if not root: return 0

      leftSide = max(recurse(root.left), 0)
      rightSide = max(recurse(root.right), 0)
      
      self.globalMaximumSum = max(self.globalMaximumSum, rightSide + leftSide + root.val)

      return max(leftSide, rightSide) + root.val

    recurse(root)

    return self.globalMaximumSum

