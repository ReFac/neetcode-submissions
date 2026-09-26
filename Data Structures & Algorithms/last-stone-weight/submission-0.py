class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-stone for stone in stones]
        heapq.heapify(heap)
        while len(heap)>1:
            x = heapq.heappop(heap)
            y = heap[0]
            if x==y:
                heapq.heappop(heap)
            else:
                z = x-y
                heapq.heapreplace(heap,z)
        
        if heap:
            return -heap[0]
        else:
            return 0
        