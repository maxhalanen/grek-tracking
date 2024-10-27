from collections import deque

#class TreeNode:
#  def __init__(self, val):
#    self.val = val
#    self.left, self.right, self.next = None, None, None


class Solution:
  def connect(self, root):

    deq = deque()
    deq.append(root)
    prevNode = None

    while deq:

      layerLen = len(deq)

      for _ in range(layerLen):
        
        currNode = deq.popleft()

        if currNode.left:
          deq.append(currNode.left)
        if currNode.right:
          deq.append(currNode.right)

        if prevNode:
          prevNode.next = currNode 
        prevNode = currNode       

    return root

