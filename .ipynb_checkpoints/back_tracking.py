### combination -- need a better way of implementing this
class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]

        ### using backtracing
        #### problem is - how to analyze the time complexity of it
        """

        self.res = []
        tmp = []
        self.dfs(n, k, 1, 0, tmp)
        return self.res

    def dfs(self, n, k, start, current_element, tmp):
        if current_element == k:
            self.res.append(tmp[:])
            return
        for i in range(start, n+1):
            tmp.append(i)
            self.dfs(n,k, i+1, current_element+1,tmp)
            tmp.pop()

### combination sum
class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        Solution.ret = []
        if len(candidates) == 0 or target < 0:
            return Solution.ret;
        candidates = list(set(candidates))
        candidates.sort()
        tmp = []
        self.DFS(candidates, tmp, target, 0)
        return Solution.ret

    def DFS(self, candidates, tmp, target, level):
        if target == 0:
            Solution.ret.append(tmp[:])
            return
        elif target < 0:
            return
        for i in range(level, len(candidates)):
            if target < candidates[i]:
                return
            else:
                target -= candidates[i]
                tmp.append(candidates[i])
                self.DFS(candidates, tmp, target, i) # the only difference between combination is that here i is not incremented by 1
                tmp.pop()
                target += candidates[i]