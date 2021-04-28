class Solution:
    def mySqrt(self, x: int) -> int:
        return int(x ** 0.5)



# Other Solution by zharigwenda1990

class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        if x == 1:
            return 1
        
        # Find the correct partition
        last = 10
        k = 0
        while last ** (2 * k) < x:
            k += 1
            
        # Binary search within the partition
        start = 10 ** (k - 1)
        end = min(10 ** k, x)
        while start < end - 1:
            mid = (start + end) // 2
            if mid ** 2 > x:
                end = mid
            else: 
                start = mid
                
        return start