#class Node:
#  def __init__(self, value, next=None):
#    self.val = value
#    self.next = next

class Solution:
  def hasCycle(self, head):
    # TODO: Write your code here

    if head.next == None:
      return False

    slow = head

    head = head.next

    while head != slow:

      if head.next == None or head.next.next == None:
        return False
      head = head.next.next 
      slow = slow.next

    return True


