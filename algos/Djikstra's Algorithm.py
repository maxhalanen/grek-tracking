class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:

        adj = defaultdict(list)

        for s, d, w in edges:
            adj[s].append([d, w])

        seen = {}
        minHeap = [[0, src]]

        while minHeap:
            w1, n1 = heapq.heappop(minHeap)
            if n1 in seen:
                continue
            seen[n1] = w1

            for n2, w2 in adj[n1]:
                if n2 not in seen:
                    heapq.heappush(minHeap, [w1 + w2, n2])

        for i in range(n):
            if i not in seen:
                seen[i] = -1

        return seen
