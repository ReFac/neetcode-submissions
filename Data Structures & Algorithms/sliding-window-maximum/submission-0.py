class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if len(nums) < k:
            return []
        heap = []
        for i in range(0,k):
            heapq.heappush(heap,(-nums[i],i))
        result = [ -heap[0][0]]
        for i in range(k,len(nums)):
            left = i - k +1
            rightVal = nums[i]
            heapq.heappush(heap,(-rightVal,i))
            while heap[0][1] <left:
                heapq.heappop(heap)
            result.append(-heap[0][0])
        return result
            
