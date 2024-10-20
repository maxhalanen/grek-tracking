class Solution:
  def shortestDistance(self, words, word1, word2):
    # TODO: Write your code here

    n = len(words)
    ans = len(words)

    pointa = -1
    pointb = -1

    for i in range(len(words)):

        if words[i] == word1:
          pointa = i
        if words[i] == word2:
          pointb = i
    
        if pointa != -1 and pointb != -1:
          ans = min(ans, abs(pointa - pointb))
      

    return ans
