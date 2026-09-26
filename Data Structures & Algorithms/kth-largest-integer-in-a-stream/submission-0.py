class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap =[]
        for n in nums:
            self.add(n)
        

    def add(self, val: int) -> int:
        size = len(self.heap)
        if size < self.k:
            heapq.heappush(self.heap,val)
        elif self.heap[0] < val:
            heapq.heappop(self.heap)
            heapq.heappush(self.heap,val)
        return self.heap[0]

        
