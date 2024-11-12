class Solution: 
    def decimalToBinary(self, num):
        
        stack = []
        str1 = ''

        while True:
            stack.append(num % 2)
            if num <= 1:
                break
            num //= 2

        return ''.join(str(i) for i in reversed(stack))


