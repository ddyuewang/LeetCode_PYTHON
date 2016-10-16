class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int

        # alternative is to use the sum (0 to n) = n*(n+1)/2
        """
        """
        # This doesnt consider the boundary case
        x1 = nums[0]
        x2 = 0
        n  = len(nums) + 1
        for num in nums[1:]:
            x1 = x1^num
        for i in xrange(1,n+1):
            x2 = x2^i
        return (x1^x2)

        """

        a = reduce(operator.xor, nums)
        b = reduce(operator.xor, range(len(nums) + 1))
        return a ^ b