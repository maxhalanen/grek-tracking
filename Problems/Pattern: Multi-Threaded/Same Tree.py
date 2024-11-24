# class TreeNode:
#     def __init__(self, val):
#         self.val = val
#         self.left = None
#         self.right = None

class Solution:
  def isSameTree(self, p, q):
    
    def traverse(p, q):
      
      if not p and not q:
        return True

      if not p or not q:
        return False
      
      if p.val != q.val:
        return False

      return traverse(p.left, q.left) and traverse(p.right, q.right)


    return traverse(p, q)
