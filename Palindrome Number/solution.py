class Solution:
    def isPalindrome(self, x: int) -> bool:
        str_x = str(x)
        len_x = len(str_x)
        
        for i in range(len_x//2):
            if str_x[i] != str_x[-(i+1)]:
                return False
        return True