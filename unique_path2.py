class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        ##### v1. solution that save the results

    #     # get the dimension
    #     m = len(obstacleGrid)
    #     n = len(obstacleGrid[0])
    #     Solution.res = {}
    #     ### initialization phase - not necessary all 1
    #     for i in range(n):
    #         if obstacleGrid[0][i] == 1:
    #             break;
    #         Solution.res[(0,i)] = 1
    #     for i in range(m):
    #         if obstacleGrid[i][0] == 1:
    #             break;
    #         Solution.res[(i,0)] = 1
    #     return self.dfs(obstacleGrid, m-1, n-1)

    # def dfs(self, obstacleGrid, x, y):
    #     if obstacleGrid[0][0] == 1 or obstacleGrid[x][y] == 1:
    #         return 0
    #     if x<0 or y<0:
    #         return 0
    #     if x==0 and y==0:
    #         return 1

    #     if (x,y) in Solution.res.keys():
    #         return Solution.res[(x,y)]
    #     else:
    #         Solution.res[(x,y)] = self.dfs(obstacleGrid,x-1,y) + self.dfs(obstacleGrid,x,y-1)
    #         return Solution.res[(x,y)]
        
        ######----------------------------------------
        # v2. using single list - DP
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        #### deal with boundary case
        if m == 1 or n == 1:
           if 1 not in obstacleGrid[0] and [1] not in obstacleGrid:
               return 1
           else:
               return 0
        #### boundary condition
        if obstacleGrid[0][0] == 1 or obstacleGrid[m-1][n-1] == 1:
             return 0

        Solution.res = [0] * n # just use one single list - in n direction
        if obstacleGrid[0][0] == 0:
            Solution.res[0] = 1
        else:
            Solution.res[0] = 0

        for i in range(m):
            if Solution.res[0] != 0 and obstacleGrid[i][0] ==0:
                Solution.res[0] = 1
            else:
                Solution.res[0] = 0
            for j in range(1,n):
                if (obstacleGrid[i][j] == 0):
                    Solution.res[j] = Solution.res[j] + Solution.res[j-1]
                else:
                    Solution.res[j] = 0
        return Solution.res[n-1]