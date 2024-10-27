from collections import deque


#class TreeNode:
#  def __init__(self, val):
#    self.val = val
#    self.left, self.right = None, None


class Solution:
  def findSuccessor(self, root, key):
    
    queue = deque()
    queue.append(root)
    nextNode = False
    while queue:

      layer = len(queue)

      for _ in range(layer):

        currNode = queue.popleft()
        
        if nextNode: return currNode

        if currNode.val == key:
          nextNode = True

        if currNode.left:
          queue.append(currNode.left)
        if currNode.right:
          queue.append(currNode.right)

    return root
