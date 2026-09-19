class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        columns = defaultdict(set)
        boxes = defaultdict(set)
        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val == ".":
                    continue
                
                key = (r//3,c//3)
                if val in rows[r] or val in columns[c] or val in boxes[key]:
                    return False
                
                rows[r].add(val)
                columns[c].add(val)
                boxes[key].add(val)
        
        return True
                
        
        