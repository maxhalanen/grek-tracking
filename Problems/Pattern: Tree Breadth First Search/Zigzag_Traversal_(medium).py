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
    
    zigzag = False

    while deq:

      layerLen = len(deq)
      layerNodes = deque()

      for _ in range(layerLen):

        currNode = deq.popleft()

        if zigzag:
          layerNodes.appendleft(currNode.val)
        else:
          layerNodes.append(currNode.val)

        if currNode.left:
          deq.append(currNode.left)
        if currNode.right:
          deq.append(currNode.right)
      zigzag = not zigzag
      result.append(list(layerNodes))
      
    return result
