class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        subset = []
        length = len(candidates)
        candidates.sort()
        
        def dfs (i,remain):
            if remain == 0:
                if subset not in result:
                    result.append(subset.copy())
                return 
            if remain < 0 or i >= length:
                return
            subset.append(candidates[i])
            dfs(i+1,remain-candidates[i])
            subset.pop()
            dfs(i+1,remain)
        dfs(0,target)
        return result

            
            

        