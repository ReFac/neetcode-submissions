class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        c = len(board[0])
        r = len(board)
        size = len(word)

        def dfs(i,j,idx):
            if i<0 or j<0 or i>=r or j>=c or board[i][j]!=word[idx]:
                return False
            if idx == size - 1:
                return True
            temp = board[i][j]
            board[i][j]

            check = dfs(i+1,j,idx+1) or dfs(i,j+1,idx+1) or dfs(i-1,j,idx+1) or dfs(i,j-1,idx+1)

            board[i][j] = temp


            return check
            
        for i in range(r):
            for j in range(c):
                if board[i][j] == word[0]:
                    if dfs(i,j,0):
                        return True


        return False