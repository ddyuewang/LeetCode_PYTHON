class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int

        ### v1. recursion solution
        """
        # if m < 1 or n < 1:
        #     return 0
        # if m == 1 and n == 1:
        #     return 1

        # return self.uniquePaths(m-1,n) + self.uniquePaths(m,n-1)
        # －－－－－－－－－－－－－－－－－－－－－－－－－－－－－－＃
        ######## Please note in this question all the results initialized to be 1, rather than steps @@@########

        #### v2.save the table to avoid the duplicate
    #     Solution.res = {}
    #     for i in raange(n):
    #         Solution.res[(0,i)] = 1
    #     for i in range(m):
    #         Solution.res[(i,0)] = 1
    #     return self.dfs(m-1, n-1)

    # def dfs(self, x, y):
    #     if x<0 or y<0:
    #         return
    #     if x==0 and y==0:
    #         return 1
    #     if (x,y) in Solution.res.keys():
    #         return Solution.res[(x,y)]
    #     else:
    #         Solution.res[(x,y)] = self.dfs(x-1,y) + self.dfs(x,y-1)
    #         return Solution.res[(x,y)]

        ############################

        ### v3. dynamic programming version - O(n^2) - time complexity, O(n) - space complexity
        # Solution.res = [0] * n # just use one single list - in n direction
        # Solution.res[0] = 1

        # for i in range(m):
        #     for j in range(1,n):
        #         Solution.res[j] = Solution.res[j] + Solution.res[j-1]

        # return Solution.res[n-1]

        #### v3_2 @ in m direction
        Solution.res = [0] * m # just use one single list - in n direction
        Solution.res[0] = 1

        for i in range(n):
            for j in range(1,m):
                Solution.res[j] = Solution.res[j] + Solution.res[j-1]

        return Solution.res[m-1]

