from collections import deque

#class TreeNode:
#  def __init__(self, val):
#    self.val = val
#    self.left, self.right = None, None

class Solution:
  def traverse(self, root):

    result = deque()

    deq = deque()
    deq.append(root)

    while deq:

      layerStorage = []
      layerLen = len(deq)

      for _ in range(layerLen):

        currNode = deq.popleft()
        layerStorage.append(currNode.val)

        if currNode.left:
          deq.append(currNode.left)
        if currNode.right:
          deq.append(currNode.right)
      
      result.appendleft(layerStorage)
    
    temp = [list(sublist) for sublist in result]

    return temp
