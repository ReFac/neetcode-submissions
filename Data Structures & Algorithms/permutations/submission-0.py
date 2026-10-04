class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        sub = []
        size = len(nums)
        used = [False] * size

        def backtrack():
            if len(sub) == size:
                result.append(sub.copy())
                return
            for i in range(size):
                if used[i]:
                    continue
                sub.append(nums[i])
                used[i] = True
                backtrack()
                sub.pop()
                used[i] = False

        
        backtrack()
        return result

                

            

        
        