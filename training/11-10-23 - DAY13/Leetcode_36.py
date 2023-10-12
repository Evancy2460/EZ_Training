#36. Valid Sudoku
import collections
class Solution:
    def isValidSudoku(self, l: List[List[str]]) -> bool:
        row=collections.defaultdict(set)
        col=collections.defaultdict(set)
        box=collections.defaultdict(set) 
        for i in range(9):
            for j in range(9):
                if l[i][j]!='.':
                    if l[i][j] in row[i] or l[i][j] in col[j] or l[i][j] in box[(i//3,j//3)]:
                        return False
                    row[i].add(l[i][j])
                    col[j].add(l[i][j])
                    box[(i//3,j//3)].add(l[i][j])
        return True
                    
        
