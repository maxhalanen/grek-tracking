#class TreeNode:
#  def __init__(self, val, left=None, right=None):
#    self.val = val
#    self.left = left
#    self.right = right

class Solution:
  def findSumOfPathNumbers(self, root):
    
    sum = [0]

    def recurse(root, num):

      if not root:
        return

      num = num * 10 + root.val
      
      if root.left == None and root.right == None:
        sum[0] += num
        return  
      
      recurse(root.left, num)
      recurse(root.right, num)
    
    num = 0
    recurse(root, num)

    return sum[0]


