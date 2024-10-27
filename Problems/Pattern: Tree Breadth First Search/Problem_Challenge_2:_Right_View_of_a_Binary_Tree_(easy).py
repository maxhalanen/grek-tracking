from collections import deque

#class TreeNode:
#  def __init__(self, val):
#    self.val = val
#    self.left, self.right = None, None

class Solution:
  def traverse(self, root):
    result = []

    deq = deque()
    deq.append(root)

    while deq:
      
      lenLayer = len(deq)

      for i in range(lenLayer):
        
        currNode = deq.popleft()

        if i == lenLayer - 1:
          result.append(currNode.val)

        if currNode.left:
          deq.append(currNode.left)
        if currNode.right:
          deq.append(currNode.right)
        
    return result
