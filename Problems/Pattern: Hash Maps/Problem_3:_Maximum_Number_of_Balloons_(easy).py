from collections import defaultdict

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        
        map = defaultdict(int)
        
        min_count = math.inf

        for i in text:
            map[i] = map.get(i, 0) + 1
        
        min_count = min(min_count, map['b'])
        min_count = min(min_count, map['a'])
        min_count = min(min_count, map['l'] // 2)
        min_count = min(min_count, map['o'] // 2)
        min_count = min(min_count, map['n'])

        return min_count

