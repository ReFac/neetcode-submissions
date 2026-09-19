class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        buckets = [[] for _ in range(len(nums)+1)]
        for val, frq in count.items():
            buckets[frq].append(val)
        result = []
        for i in range(len(buckets)-1,0,-1):
            for val in buckets[i]:
                result.append(val)
                if len(result) == k:
                    return result
        return result

            