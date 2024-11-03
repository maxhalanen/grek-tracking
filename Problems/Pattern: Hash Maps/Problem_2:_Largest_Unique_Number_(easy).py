from collections import defaultdict

class Solution:
    def largestUniqueNumber(self, A: List[int]) -> int:
        
        maxUnique = -1
        freq = {}

        for i in A:
            freq[i] = freq.get(i, 0) + 1
        
        for n in A:
            if freq[n] == 1:
                maxUnique = max(n, maxUnique)  

        return maxUnique
