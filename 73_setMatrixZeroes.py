class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        first_row_zero = False
        for m in range(len(matrix)):
            for n in range(len(matrix[0])):
                if matrix[m][n] == 0:
                    matrix[m][0] = 0
                    
                    if n == 0: first_row_zero = True
                    else:      matrix[0][n] = 0
                    
        
        for m in range(1, len(matrix)):
            for n in range(1, len(matrix[0])):
                if matrix[m][0] == 0 or matrix[0][n] == 0:
                    matrix[m][n] = 0

        for n in range(1, len(matrix[0])):
            if matrix[0][n] == 0:
                for m in range(len(matrix)):
                    matrix[m][n] = 0
        
        if matrix[0][0] == 0:
            for i in range(len(matrix[0])):
                matrix[0][i] = 0
        
        if first_row_zero:
            for i in range(len(matrix)):
                matrix[i][0] = 0
