class Solution:
    def nextLargerElement(self, arr):
        
        res = [0]*len(arr)

        stack = []

        for i in range(len(arr)-1, -1, -1):

            if len(stack) == 0:
                res[i] = -1
                stack.append(arr[i])
                continue

            if arr[i] < stack[-1]:
                res[i] = stack[-1]

            while arr[i] >= stack[-1]:
                stack.pop(-1)
                if len(stack) == 0:
                    res[i] = -1
                    break
                elif arr[i] < stack[-1]:
                    res[i] = stack[-1]
                
            stack.append(arr[i])

        return res
