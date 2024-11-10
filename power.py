class Solution:

    def myPow(self, x: float, n: int) -> float:
        if n == 1:
            return x
        if n == -1:
            return 1/x
        if n % 2 == 0:
            return Solution().myPow(x, n // 2) * Solution().myPow(x, n // 2)
        else:
            return Solution().myPow(x, (n - 1) // 2) * Solution().myPow(x, (n - 1) // 2) * x


print(Solution().myPow(x=2.00000, n=-2))
