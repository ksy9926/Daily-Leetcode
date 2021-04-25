class Solution:
    def addBinary(self, a: str, b: str) -> str:
        sum_a = 0
        sum_b = 0
        
        for i in range(len(a)-1, -1, -1):
            sum_a += (2 ** i) * int(a[len(a)-1 - i])
            
        for j in range(len(b)-1, -1, -1):
            sum_b += (2 ** j) * int(b[len(b)-1 - j])
            
        sum_all = sum_a + sum_b
        result = ''
        
        if sum_all == 0:
            return '0'
        
        while sum_all != 0:
            result = str(sum_all % 2) + result
            sum_all = sum_all // 2
        
        return result


# Other solution

# by pillaikartik10
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return bin(int(a,2) + int(b,2))[2:]