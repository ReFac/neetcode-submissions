class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        subset = []
        result = []
        size = len(nums)
        nums.sort()

        def dfs(i):
            if i == size:
                result.append(subset.copy())
                return

            subset.append(nums[i])
            dfs(i+1)
            subset.pop()
            while i< (size-1) and nums[i] == nums[i+1]:
                i = i+1
            dfs(i+1)


        dfs(0)
        return result