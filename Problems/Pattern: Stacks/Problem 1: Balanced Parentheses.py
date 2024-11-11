class Solution:
    def isValid(self, s):
        
        stack = []
        opening = {"{", "[", "("}
        map = {"}":"{", "]":"[", ")":"("}
        
        for i in s:
            if i in opening:
                stack.append(i)
            if i in map:
                if map[i] == stack[-1]:
                    stack.pop(-1)
                else:
                    return False
                    
        if stack:
            return False
        return True
