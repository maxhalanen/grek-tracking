class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

        adj = defaultdict(list)

        for s, e, w in times:
            adj[s].append([e, w])

        seen = {}
        maxTime = 0
        minHeap = [[0, k]]

        while minHeap:
            w1, n1 = heapq.heappop(minHeap)
            if n1 in seen:
                continue
            seen[n1] = w1

            maxTime =  max(maxTime, w1)
            
            for n2, w2 in adj[n1]:
                if n2 not in seen:
                    heapq.heappush(minHeap, [w1 + w2, n2])
        
        return maxTime if len(seen) == n else -1
                

        
