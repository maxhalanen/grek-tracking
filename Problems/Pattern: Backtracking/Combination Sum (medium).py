class Solution:
  def combinationSum(self, candidates, target):
    
    res = []  

    start = 0

    def backtrack(candidates, target, res, start, comb):

      if target == 0:
        res.append(list(comb))
        return

      for i in range(start, len(candidates)):
        
        if target < candidates[i]:
          continue
        
        comb.append(candidates[i])

        backtrack(candidates, target - candidates[i], res, i, comb)

        comb.pop()

    backtrack(candidates, target, res, 0, [])

    return res
