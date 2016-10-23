### combination -- need a better way of implementing this
# class Solution_1(object):
#     def combine(self, n, k):
#         """
#         :type n: int
#         :type k: int
#         :rtype: List[List[int]]
#
#         ### using backtracing
#         #### problem is - how to analyze the time complexity of it
#         """
#
#         self.res = []
#         tmp = []
#         self.dfs(n, k, 1, 0, tmp)
#         return self.res
#
#     def dfs(self, n, k, start, current_element, tmp):
#         if current_element == k:
#             self.res.append(tmp[:])
#             return
#         for i in range(start, n+1):
#             tmp.append(i)
#             self.dfs(n,k, i+1, current_element+1,tmp)
#             tmp.pop()

### combination sum
# class Solution_2(object):
#     def combinationSum(self, candidates, target):
#         """
#         :type candidates: List[int]
#         :type target: int
#         :rtype: List[List[int]]
#         """
#         Solution.ret = []
#         if len(candidates) == 0 or target < 0:
#             return Solution.ret;
#         candidates = list(set(candidates))
#         candidates.sort()
#         tmp = []
#         self.DFS(candidates, tmp, target, 0)
#         return Solution.ret
#
#     def DFS(self, candidates, tmp, target, level):
#         if target == 0:
#             Solution.ret.append(tmp[:])
#             return
#         elif target < 0:
#             return
#         for i in range(level, len(candidates)):
#             if target < candidates[i]:
#                 return
#             else:
#                 target -= candidates[i]
#                 tmp.append(candidates[i])
#                 self.DFS(candidates, tmp, target, i) # the only difference between combination is that here i is not incremented by 1
#                 tmp.pop()
#                 target += candidates[i]

# combination sum II
class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        Solution.ret = []
        if len(candidates) == 0 or target < 0:
            return Solution.ret;
        # candidates = list(set(candidates)) # eliminate the duplicate
        candidates.sort()
        tmp = []
        flag = [0] * len(candidates)
        self.DFS(candidates, tmp, target, 0, flag)
        return Solution.ret

    def DFS(self, candidates, tmp, target, level, flag):
        if target == 0:
            Solution.ret.append(tmp[:])
            return
        elif target < 0:
            return
        for i in range(level, len(candidates)):
            if target < candidates[i]:
                return
            if i <= len(candidates)-1 and i >= 1 and candidates[i] == candidates[i-1] and flag[i-1] == 0: # key difference
                continue
            else:
                target -= candidates[i]
                tmp.append(candidates[i])
                flag[i] = 1
                self.DFS(candidates, tmp, target, i+1, flag) # the only diff between combination sum
                tmp.pop()
                flag[i] = 0
                target += candidates[i]

                # #### THE following doesnt work b/c it doesnt treat the same number differently
                # while (i < len(candidates)-1) and (candidates[i] == candidates[i+1]):
                # # we add this while loop is to skip the duplication res
                #     i=i+1;

                ### input  [10,1,2,7,6,1,5]  # 8
                ### output [[1,1,6],[1,2,5],[1,7],[1,2,5],[1,7],[2,6]]
                ### [1,2,5] comes from the 1st one and 2nd one respectively, without a flag wont be able to differently