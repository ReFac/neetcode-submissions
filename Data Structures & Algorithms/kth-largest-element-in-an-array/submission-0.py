class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []

        def add(num):
            if len(heap)<k:
                heapq.heappush(heap,num)
            else:
                if heap[0] < num:
                    heapq.heapreplace(heap,num)

        for num in nums:
            add(num)

        return heap[0]
        