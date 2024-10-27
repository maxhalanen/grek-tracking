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

      layerLen = len(deq)
      layerStore = []

      for _ in range(layerLen):
        
        currNode = deq.popleft()

        layerStore.append(currNode.val)

        if currNode.left:
          deq.append(currNode.left)
        if currNode.right:
          deq.append(currNode.right)

      result.append(layerStore)
    
    return result
