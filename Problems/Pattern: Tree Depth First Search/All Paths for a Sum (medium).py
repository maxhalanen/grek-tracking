#class TreeNode:
#  def __init__(self, val, left=None, right=None):
#    self.val = val
#    self.left = left
#    self.right = right

class Solution:
  def findPaths(self, root, required_sum):
    allPaths = []
    
    def recurse(root, sum, curr_path):
      
      if root == None:
        return 
      
      curr_path.append(root.val)
      
      if root.right == None and root.left == None and root.val == sum:
        allPaths.append(curr_path)
        return 

      recurse(root.left, sum - root.val, list(curr_path))
      recurse(root.right, sum - root.val, list(curr_path))
    
      return 

    curr_path = []
    recurse(root, required_sum, curr_path)


    return allPaths
