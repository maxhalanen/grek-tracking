class Solution:
  def reverseVowels(self, s: str) -> str:
    # TODO: Write your code here

    x = list(s)

    pointa = 0
    pointb = len(s) - 1

    vowela = False
    vowelb = False
    
    vowels = {'a', 'e', 'i', 'o', 'u','A', 'E', 'I', 'O', 'U'}

    while pointa < pointb:

      if x[pointa] in vowels:
        vowela = True
      if x[pointb] in vowels:
        vowelb = True
      
      if vowela == True:
        pass
      else:
        pointa += 1
      
      if vowelb == True:
        pass
      else:
        pointb -= 1
      
      if vowela == True and vowelb == True:
        temp = x[pointa]
        x[pointa] = x[pointb]
        x[pointb] = temp

        pointa += 1
        pointb -= 1
      
      vowela = False
      vowelb = False
    
    return ''.join(x)
