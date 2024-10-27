from collections import deque


#class TreeNode:
#  def __init__(self, val):
#    self.val = val
#    self.left, self.right = None, None

class Solution:
  def findDepth(self, root):
    
    minimumTreeDepth = 1

    deq = deque()
    deq.append(root)

    while deq:

      layer = len(deq)

      for _ in range(layer):

        currNode = deq.popleft()

        if not currNode.left and not currNode.right:
          return minimumTreeDepth

        if currNode.left:
          deq.append(currNode.left)

        if currNode.right:
          deq.append(currNode.right)

      minimumTreeDepth += 1
    
    return minimumTreeDepth
