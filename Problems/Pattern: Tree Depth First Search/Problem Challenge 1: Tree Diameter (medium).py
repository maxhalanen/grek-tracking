#class TreeNode:
#  def __init__(self, val, left=None, right=None):
#    self.val = val
#    self.left = left
#    self.right = right


class Solution:

  def findDiameter(self, root):

    self.treeDiameter = 0;

    def recurse(root):

      if not root:
        return 0

      self.treeDiameter = max(depth(root.left, 1) + depth(root.right, 1) + 1, self.treeDiameter)

      recurse(root.left)
      recurse(root.right)

    def depth(root, dp):

      if not root:
        return dp
      
      if not root.left and not root.right:
        return dp

      return max(depth(root.left, dp + 1), depth(root.right, dp + 1))


    recurse(root)

    return self.treeDiameter
