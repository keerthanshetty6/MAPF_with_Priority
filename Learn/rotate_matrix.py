class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)

        #Transpose
        for i in range(n//2 +1):
            for j in range(i+1,n):
                matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]

        #Reflect
        for i in range(n):
            s=0
            e=len(matrix[0])-1
            while s<e:
                matrix[i][s],matrix[i][e]=matrix[i][e],matrix[i][s]
                s+=1
                e-=1
        return matrix

matrix =[[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]]
sol=Solution()
print(sol.rotate(matrix))