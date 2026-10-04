class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        for n in nums:
            subset = []
            for x in res:
                subset.append(x + [n])
            res = res + subset
        return res

            