class Solution:
    def reverseString(self, s):
        
        stack = []

        for i in range(len(s)-1, -1, -1):
            stack.append(s[i])
        
        return "".join(stack)


