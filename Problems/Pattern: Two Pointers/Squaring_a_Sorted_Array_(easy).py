class Solution:
  def makeSquares(self, arr):
    n = len(arr)
    squares = [x for x in range(n)]
    
    pointa = 0
    pointb = len(arr) - 1

    endpoint = len(arr) - 1

    while pointa <= pointb and endpoint >= 0: 

      if abs(arr[pointa]) < abs(arr[pointb]):
        squares[endpoint] = arr[pointb]**2
        pointb -= 1
        endpoint -= 1
      elif abs(arr[pointa]) >= abs(arr[pointb]):
        squares[endpoint] = arr[pointa]**2
        pointa += 1
        endpoint -= 1
      

    return squares
