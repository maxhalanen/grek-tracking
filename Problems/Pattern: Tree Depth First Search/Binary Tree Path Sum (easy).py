#class TreeNode:
#  def __init__(self, val, left=None, right=None):
#    self.val = val
#    self.left = left
#    self.right = right

class Solution:
  def hasPath(self, root, sum):
    
    def recurse(root, sum):

      if root == None:
        return False
      
      if root.val == sum and root.left == None and root.right == None:
        return True

      return recurse(root.left, sum - root.val) or recurse(root.right, sum - root.val)
  
    return recurse(root, sum)
