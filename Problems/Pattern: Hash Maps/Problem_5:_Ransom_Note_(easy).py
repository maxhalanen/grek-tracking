from collections import Counter

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # Counter is a default dict
        ransom = Counter(ransomNote)
        maga = Counter(magazine)

        for i in ransom:
            if ransom[i] > maga[i]:
                return False

        return True
