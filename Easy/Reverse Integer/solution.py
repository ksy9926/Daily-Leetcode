class Solution:
    def reverse(self, x: int) -> int:
        str_x = str(x)
        
        if str_x[0] != '0':
            result = str_x[-1]
        elif str_x == '0':
            result = '0'
        else:
            result = ''
        
        for i in range(1, len(str_x)):
            result += str_x[-(i+1)]
        
        if result[-1] == '-':
            result = -int(result.replace("-", ""))
        else:
            result = int(result)
            
        if -(2**31) <= result <= (2**31)-1:
            return result
        else:
            return 0