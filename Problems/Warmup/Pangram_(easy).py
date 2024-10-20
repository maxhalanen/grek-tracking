class Solution:
  def checkIfPangram(self, sentence):
    

    x = sorted(list(sentence.lower()))

    alphaset = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'}
    xset = set()

    for i in x:
      if i in alphaset:

        xset.add(i)


    if alphaset == xset:
      return True 

    return False
