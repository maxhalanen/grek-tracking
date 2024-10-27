from collections import deque

#class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = self.right = self.next = None

class Solution:
    def connect(self, root):
        
        deq = deque()
        deq.append(root)
        prevNode = None

        while deq:
            
            layerLen = len(deq)

            for i in range(layerLen):
                
                currNode = deq.popleft()

                if currNode.left:
                    deq.append(currNode.left)
                
                if currNode.right:
                    deq.append(currNode.right)

                if prevNode:
                    prevNode.next = currNode
                prevNode = currNode
            prevNode = None
                
        return root

