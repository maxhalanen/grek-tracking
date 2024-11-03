from collections import defaultdict
from collections import deque

class Solution:
    def validPath(self, n: int, edges: [[int]], start: int, end: int) -> bool:
        
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u) 
        
        visited = set()
        q = deque()
        q.append(start)

        while q:
            currNode = q.popleft()
            if currNode == end:
                return True

            for adjNode in graph[currNode]:
                
                if adjNode not in visited:
                    q.append(currNode)
                    visited.add(currNode)

        return False;

    

