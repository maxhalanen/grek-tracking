#class Node:
#  def __init__(self, value, next=None):
#    self.val = value
#    self.next = next

class Solution:
  def findMiddle(self, head):

    fast = head

    while fast.next != None:
      if fast.next.next == None:
        head = head.next
        break
      head = head.next
      fast = fast.next.next


    return head
