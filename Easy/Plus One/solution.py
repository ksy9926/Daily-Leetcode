class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        all_digits = "".join(map(str, digits))
        all_digits = str(int(all_digits) + 1)
        result = []
        
        for i in range(len(all_digits)):
            result.append(int(all_digits[i]))
        
        return result


# Other Solution

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        dig = "".join(str(i) for i in digits)
        int_dig = int(dig)+1
        return list(map(int,str(int_dig)))