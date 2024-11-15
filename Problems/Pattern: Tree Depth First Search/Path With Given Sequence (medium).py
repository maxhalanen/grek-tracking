#class TreeNode:
#  def __init__(self, val, left=None, right=None):
#    self.val = val
#    self.left = left
#    self.right = right

class Solution:
  def findPath(self, root, sequence):

    def recurse(root, iteration):
      
      if iteration >= len(sequence):
        return False

      if root == None:
        return False

      if root.val != sequence[iteration]:
        return False

      if root.right == None and root.left == None:
        return True
      
      return recurse(root.left, iteration+1) or recurse(root.right, iteration+1)

    iteration = 0

    return recurse(root, iteration)
