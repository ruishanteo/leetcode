class Solution(object):
    def floodFill(self, image, sr, sc, color):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type color: int
        :rtype: List[List[int]]
        """
        original = image[sr][sc]
        def helper(matrix, r, c):
            if (r < 0 or r >= len(matrix) or c < 0 or c >= len(matrix[0])):
                return
            
            if (matrix[r][c] != original):
                return
            
            if (matrix[r][c] == color):
                return
            
            matrix[r][c] = color
            helper(matrix, r - 1, c)
            helper(matrix, r + 1, c)
            helper(matrix, r, c - 1)
            helper(matrix, r, c + 1)
            
        helper(image, sr, sc)
        return image