class Solution:
    def __init__(self):
        self.memo = {}
        
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        elif n == 2:
            return 2
        if n in self.memo:
            return self.memo[n]
        
        self.memo[n] = self.climbStairs(n-1) + self.climbStairs(n-2)
        
        return self.memo[n]


# Other solution by dustlihy

class Solution:
    def climbStairs(self, n: int) -> int:
        x, y = 1, 1
        for i in range(2, n+1):
            x, y = y, x+y
        return y