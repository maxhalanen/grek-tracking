#class Node:
#  def __init__(self, value, next=None):
#    self.val = value
#    self.next = next



class Solution:
  def reorder(self, head):

    if head.next == None:
      return head

    fast = head
    slow = head
    prev = None

    while fast and fast.next:
      prev = slow
      fast = fast.next.next
      slow = slow.next
   
    prev.next = None

    secondHalf = self.reverseLList(slow)

    ans = self.join(head, secondHalf)

    return ans

  def join(self, firstHalf, secondHalf):
      start = firstHalf

      while secondHalf and firstHalf:

          firstHalfNext = firstHalf.next
          secondHalfNext = secondHalf.next

          firstHalf.next = secondHalf

          if firstHalfNext:
            secondHalf.next = firstHalfNext

          firstHalf = firstHalfNext
          secondHalf = secondHalfNext
      
      return start

  def reverseLList(self, head):

    prev = None
    current = head

    while current:
      nextNode = current.next
      current.next = prev
      prev = current
      current = nextNode
    
    return prev


