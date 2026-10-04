class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        subset = []
        length = len(candidates)
        candidates.sort()
        
        def dfs (i,remain):
            if remain == 0:
                result.append(subset.copy())
                return 
            if remain < 0 or i >= length:
                return
            subset.append(candidates[i])
            dfs(i+1,remain-candidates[i])
            subset.pop()
            while i+1 < length and candidates[i+1] == candidates[i]:
                i = i+1
            dfs(i+1,remain)
        dfs(0,target)
        return result

            
            

        