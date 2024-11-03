class Solution:
    def firstUniqChar(self, s: str) -> int:

        map = {}

        for i in range(len(s)):
            char = s[i]
            if char in map:
                map[char] = len(s)
            else:
                map[char] = i
        
        minIndex = math.inf

        for i in map:
            minIndex = min(minIndex, map[i])

        if minIndex == len(s):
            return -1

        return minIndex

