class Solution:
    def longestPalindrome(self, s: str) -> int:      

        #populate map without Counter    
        #freq = {}
        #for i in s:
            #freq[i] = freq.get(i, 0) + 1
    
        from collections import Counter

        freq = Counter(s)
        length = 0
        odd = False

        for i in freq:
            if freq[i] % 2 == 1:
                odd = True
                length += freq[i] - 1
            else:
                length += freq[i]
        
        if odd:
           length += 1

        return length
