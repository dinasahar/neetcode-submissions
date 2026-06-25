class Solution:
    def has_duplicate(self, values):
        values = [x for x in values if x != "."]
        return len(values) != len(set(values))

    def row_col(self, board):
        for i in range(9):
            row = board[i]
            col = [board[r][i] for r in range(9)]

            if self.has_duplicate(row) or self.has_duplicate(col):
                return False

        return True

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        if self.row_col(board) == False:
            return False

        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                box = []

                for r in range(i, i + 3):
                    for c in range(j, j + 3):
                        box.append(board[r][c])

                if self.has_duplicate(box):
                    return False

        return True