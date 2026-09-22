class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        maxheap =[]
        lenNums = len(nums)
        result = []
        if k > lenNums:
            return result
        for i in range(0,k):
            heapq.heappush(maxheap,(-nums[i],i))
        result.append(-maxheap[0][0])
        for i in range(k,lenNums):
            heapq.heappush(maxheap,(-nums[i],i))
            while maxheap[0][1] <= i-k: 
                heapq.heappop(maxheap)
            result.append(-maxheap[0][0])

        return result


        
        