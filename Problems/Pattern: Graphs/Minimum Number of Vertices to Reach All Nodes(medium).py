from typing import List

class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:

        nodes_with_incoming = set()

        for _, inc in edges:
            nodes_with_incoming.add(inc)
                
        return [i for i in range(n) if i not in nodes_with_incoming]
