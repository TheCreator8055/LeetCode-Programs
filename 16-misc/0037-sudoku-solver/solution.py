class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        # 1. State tracking using bitmasks for O(1) lookups
        rows = [0] * 9
        cols = [0] * 9
        boxes = [0] * 9
        empty_cells = []

        for r in range(9):
            for c in range(9):
                if board[r][c] == '.':
                    empty_cells.append((r, c))
                else:
                    digit = int(board[r][c])
                    mask = 1 << digit
                    rows[r] |= mask
                    cols[c] |= mask
                    boxes[(r // 3) * 3 + (c // 3)] |= mask

        def backtrack(index):
            if index == len(empty_cells):
                return True
            
            r, c = empty_cells[index]
            box_idx = (r // 3) * 3 + (c // 3)
            
            # 2. Try digits 1-9
            for digit in range(1, 10):
                mask = 1 << digit
                # O(1) Validity Check
                if not (rows[r] & mask or cols[c] & mask or boxes[box_idx] & mask):
                    # Set state
                    board[r][c] = str(digit)
                    rows[r] |= mask
                    cols[c] |= mask
                    boxes[box_idx] |= mask
                    
                    if backtrack(index + 1):
                        return True
                    
                    # Backtrack (Reset state)
                    rows[r] ^= mask
                    cols[c] ^= mask
                    boxes[box_idx] ^= mask
                    board[r][c] = '.'
            return False

        backtrack(0)

