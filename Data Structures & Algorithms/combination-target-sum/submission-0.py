class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        subset = []
        size = len(nums)
        def dfs(i,remain):
            if remain == 0:
                result.append(subset.copy())
                return
            if i >= size or remain < 0:
                return
            subset.append(nums[i])
            dfs(i,remain - nums[i])
            subset.pop()
            dfs(i+1,remain)

        dfs(0,target)
        return result