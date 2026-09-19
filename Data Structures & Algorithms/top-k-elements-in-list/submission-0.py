class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        buckets = [[] for _ in range(len(nums)+1)]
        for num, frq in count.items():
            buckets[frq].append(num)
        ans = []
        for i in range(len(buckets)-1,0,-1):
            for val in buckets[i]:
                ans.append(val)
                if len(ans) >= k:
                    return ans
        return ans
        