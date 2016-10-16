class Solution(object):
    def thirdMax(self, nums):
        a = b = c = None
        if len(nums) < 3:
            return max(nums)
        else:
            for n in nums:
                if n > a:
                    b, c = a, b
                    a = n
                elif a > n > b:
                    b, c = n, b
                elif b > n > c:
                    c = n
                print n
                print "______________"
                print a, b, c
            return c if c is not None else a

if __name__ == "__main__":
    mysoln = Solution()
    mysoln.thirdMax([1,2,2,5,3,5])