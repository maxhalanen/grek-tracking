class Solution:
  def isPalindrome(self, s: str) -> bool:
    # TODO: Write your code here
      pointera = 0
      pointerb = len(s) - 1

      x = s.lower()

      while pointera < pointerb:

        if x[pointera].isalnum() == False:
          pointera += 1
          continue
        if x[pointerb].isalnum() == False:
          pointerb -= 1
          continue
        if x[pointera] == x[pointerb]:
          pointera += 1
          pointerb -= 1
          continue
        else:
          return False

      return True
