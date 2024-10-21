class Solution:
  def search(self,arr, key):

    start = 0
    end = len(arr) - 1
    mid = len(arr) // 2

    if arr[0] > arr[len(arr) - 1]:
      while start <= end:
        
        if arr[mid] > key:
          start = mid + 1
          mid = start + ((end - start) // 2)
        elif arr[mid] < key:
          end = mid - 1
          mid = start + ((end - start) // 2)
        else:
          return mid
        
      return -1 

    while start <= end:
      
      if arr[mid] < key:
        start = mid + 1
        mid = start + ((end - start) // 2)
      elif arr[mid] > key:
        end = mid - 1
        mid = start + ((end - start) // 2)
      else:
        return mid
      
    return -1 
