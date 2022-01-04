class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        
        directions = [
            (1, 0),
            (0, 1),
            (-1, 0),
            (0, -1)
        ]
        
        visited = set([(sr, sc)])
        q = [(sr, sc)]
        while q:
            row, col = q.pop(0)

            for dir in directions:
                new_row = row + dir[0]
                new_col = col + dir[1]
                
                if new_row >= len(image) or new_row < 0: continue
                if new_col >= len(image[0]) or new_col < 0: continue
                
                if (new_row, new_col) in visited: continue
                visited.add((new_row, new_col))
                
                if image[new_row][new_col] == image[sr][sc]:
                    q.append((new_row, new_col))
                    image[new_row][new_col] = newColor
                    
        image[sr][sc] = newColor
        return image
