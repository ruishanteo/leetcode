class Solution(object):
    def updateMatrix(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[List[int]]
        """
        rows = len(mat)
        cols = len(mat[0])
        q = []
        for i in range(rows):
            for j in range(cols):
                if mat[i][j] == 0:
                    q.append([i, j])
                    mat[i][j] = 0
                else:
                    mat[i][j] = "F"
        row = [-1, 1, 0, 0]
        col = [0, 0, -1, 1]
        while len(q):
            top = q.pop(0)
            x = top[0]
            y = top[1]
            for i in range(4):
                newx = x + row[i]
                newy = y + col[i]
                if newx >= 0 and newx < rows and newy >= 0 and newy < cols and mat[newx][newy] == "F":
                    mat[newx][newy] = mat[x][y] + 1
                    q.append([newx, newy])
        return mat