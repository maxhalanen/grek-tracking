#class Node:
#  def __init__(self, value, next=None):
#    self.val = value
#    self.next = next

class Solution:
  def isPalindrome(self, head):
    
    fast = head
    slow = head

    while fast != None and fast.next != None:
      fast = fast.next.next
      slow = slow.next

    
    
    reversedSecondHalf = self.reverse_LList(slow)
    firstHalf = head

    while firstHalf != None and reversedSecondHalf != None:

      if firstHalf.val != reversedSecondHalf.val:
        return False

      firstHalf = firstHalf.next
      reversedSecondHalf = reversedSecondHalf.next

    return True
  
  def reverse_LList(self, head):

    prev = None
    current = head

    while current != None:
      nextNode = current.next
      current.next = prev
      prev = current
      current = nextNode
    
    return prev
