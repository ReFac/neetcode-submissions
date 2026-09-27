class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res =[[]]
        for num in nums:
            subset = []
            for i in res:
                subset.append(i +[num])
            res += subset
        return res
        