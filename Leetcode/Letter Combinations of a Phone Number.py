class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        if digits == "":
            return []

        combos = {"2":"abc", "3":"def", "4":"ghi", "5":"jkl", "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz"}
        ans = []
        
        def recurse(string, i):

            if i == len(digits):
                ans.append(string)
                return
            
            for j in combos[digits[i]]:
                recurse(string + j, i + 1)


        recurse("", 0)

        return ans

        
