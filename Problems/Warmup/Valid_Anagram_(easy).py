class Solution:
  def isAnagram(self, s, t):
    # TODO: Write your code here

    s = list(s)
    x = sorted(s)
    t = list(t)
    y = sorted(t)


    if y == x:
      return True    

    return False
