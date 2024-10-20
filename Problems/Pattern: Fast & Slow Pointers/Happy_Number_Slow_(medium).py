class Solution:
  def find(self, num):

    if num == 1:
      return True
    elif num == 0:
      return False

    seen = set()

    use = num

    while True:


      
      seen.add(use)

      
      temp = str(use)
      happy = 0

      for i in range(len(temp)):
        happy += (int(temp[i])**2)
        print(happy)
      
      if happy == 1:
        return True

      if happy in seen:
        return False
       
      use = happy

    # TODO: Write your code here
    return False
