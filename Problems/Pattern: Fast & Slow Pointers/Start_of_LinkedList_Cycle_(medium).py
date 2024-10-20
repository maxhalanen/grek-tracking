
#class Node:
#  def __init__(self, value, next=None):
#    self.val = value
#    self.next = next

class Solution:
  def findCycleStart(self, head):
    #TODO Write your code here

    slow = head
    fast = head
    cycleLen = 0 
   
    while fast != None and fast.next != None:

      fast = fast.next.next
      slow = slow.next

      if fast == slow:
        cycleLen = self.findLength(slow)
        break

    fast = head
    slow = head

    for i in range(cycleLen):
      fast = fast.next
    
    while fast != None and fast.next != None:
      
      fast = fast.next
      slow = slow.next

      if fast==slow:
        break

    return fast


  def findLength(self, node):

    count = 0
    start = node

    while True:
      count += 1
      start = start.next
      if start == node:
        break

    return count

