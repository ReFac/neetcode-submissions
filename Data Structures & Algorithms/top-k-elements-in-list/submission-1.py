class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        heap = []
        for val, frq in count.items():
            heapq.heappush(heap,(frq,val))
            if len(heap) > k:
                heapq.heappop(heap)
        
        return [val for frq, val in heap]