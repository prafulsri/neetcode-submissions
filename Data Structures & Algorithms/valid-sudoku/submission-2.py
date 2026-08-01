class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        # rows = [set() for _ in range(9)]
        # cols = [set() for _ in range(9)]
        # boxes = [set() for _ in range(9)]
        
        rows = defaultdict(set)
        cols = defaultdict(set)
        boxes = defaultdict(set)
        

        for r in range(9):
            for c in range(9):
                val = board[r][c]
                
                # Skip empty positions
                if val == ".":
                    continue
                
                # Find the box index (0 to 8)
                box_idx = (r // 3) * 3 + (c // 3)
                
                # Check for duplicates
                if val in rows[r] or val in cols[c] or val in boxes[box_idx]:
                
                    return False
                
                # Add to trackers
                rows[r].add(val)
                cols[c].add(val)
                boxes[box_idx].add(val)
                
        return True
