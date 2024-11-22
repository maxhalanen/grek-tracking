class Solution:
  def getFactors(self, n):

    res = []

    start = 2

    def factor(comb, start, n):
      
      for i in range(start, int(n**0.5) + 1):

        if n % i == 0:

          comb.append(i)
          res.append(list(comb + [n // i]))
          factor(comb, i, n // i)
          comb.pop()

    factor([], start, n)
    return res
