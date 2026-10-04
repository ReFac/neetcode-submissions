class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        subset = []
        def dfs(i,j):
            if j == n:
                result.append("".join(subset))
                return
            
            if i < n:
                subset.append("(")
                dfs(i+1,j)
                subset.pop()

            if j < i:
                subset.append(")")
                dfs(i,j+1)
                subset.pop()
            
        dfs(0,0)
        return result

            
