class Solution:
  def search(self,arr, key):

    a = 0
    b = len(arr) - 1

    reversed_list = arr[0] < arr[len(arr) - 1]
    
    while a <= b:

      mid = (a + b) // 2
      if reversed_list:
        if arr[mid] > key:
          b = mid - 1
        elif arr[mid] < key:
          a = mid + 1
        else:
          return mid
      else:
        if arr[mid] < key:
          b = mid - 1
        elif arr[mid] > key:
          a = mid + 1
        else:
          return mid

          
    return -1 
 
