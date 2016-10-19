## generate all the permutation of a given list
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]

        # use recursion
        """

        if len(nums) <= 1:
            return [nums]
        ans = []

        for i,num in enumerate(nums):
            n = nums[:i] + nums[i+1:]
            for res in self.permute(n):
                ans.append([num] + res)
        return ans