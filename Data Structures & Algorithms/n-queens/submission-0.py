class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        cols = set()
        dia1 = set()
        dia2 = set()
        board = [["."]* n for _ in range(n)]
        result = []

        def backtrack(i):
            if i == n:
                result.append(["".join(row) for row in board])
                return

            for j in range(n):
                if j in cols or (i-j) in dia1 or (i+j) in dia2:
                    continue

                board[i][j] = "Q"
                cols.add(j)
                dia1.add(i-j)
                dia2.add(i+j)

                backtrack(i+1)

                board[i][j] = "."
                cols.remove(j)
                dia1.remove(i-j)
                dia2.remove(i+j)
        backtrack(0)
        return result
