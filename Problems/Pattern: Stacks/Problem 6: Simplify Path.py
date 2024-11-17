class Solution:
    def simplifyPath(self, path):

        stack = []
        
        for i in path.split("/"):

            if i == "..":
                if stack:
                    stack.pop()
            elif i and i != ".":
                stack.append(i)
                
        return "/"+"/".join(stack)
