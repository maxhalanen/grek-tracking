#class TreeNode:
#  def __init__(self, val, left=None, right=None):
#    self.val = val
#    self.left = left
#    self.right = right

class Solution:
  def findSumOfPathNumbers(self, root):
    
    sum = [0]

    def recurse(root, string):

      if not root:
        return
      
      string += str(root.val)

      if root.left == None and root.right == None:
        sum[0] += int(string)
        return  
      
      recurse(root.left, string)
      recurse(root.right, string)
    
    string = ""
    recurse(root, string)

    return sum[0]
