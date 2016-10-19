## pow(x, n) in log(n) time

class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float

        # break the x ^ n to (x^2)^(n/2)
        """
        if n < 0:
            return self.myPow(1/x, -n)
        elif n == 0:
            return 1
        elif n == 1:
            return x
        elif n%2 == 1:
            return x * self.myPow(x*x, (n-1)/2)
        else:
            return self.myPow(x*x,n/2)