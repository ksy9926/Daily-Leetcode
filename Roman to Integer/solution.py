class Solution:
    def romanToInt(self, s: str) -> int:
        result = 0
        roman_dict = {
            'I' : 1,
            'V' : 5,
            'X' : 10,
            'L' : 50,
            'C' : 100,
            'D' : 500,
            'M' : 1000
        }
        
        for i in range(len(s)):
            if i < len(s)-1:
                if roman_dict[s[i+1]] <= roman_dict[s[i]]:
                    result += roman_dict[s[i]]
                else:
                    result -= roman_dict[s[i]]
            else:
                result += roman_dict[s[i]]
        
        return result


# Solution by Minjee
# class Solution:
#     def romanToInt(self, s: str) -> int:
   
#         dic = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
#         x = len(s)
#         result = dic[s[x-1]]
#         for i in range(x-1,0,-1):
#             cur = dic[s[i]]
#             y = dic[s[i-1]]
#             result += y if y >= cur else -y
#         return result 