class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dic = {'}':'{', ']':'[', ')':'('}
        dicOpen = {'{', '[', '('}

        for a in s:
            if a in dicOpen:
                stack.append(a)
            else:
                if len(stack) != 0 and stack[-1] == dic[a]:
                    stack.pop()
                else:
                    return False

        if len(stack) != 0:
            return False
        return True
                

# Solution by Minjee

# class Solution:
#     def isValid(self, s: str) -> bool:
#         stack = []
#         brackets={'}':'{',
#                   ')':'(',
#                   ']':'['} 
           
#         if len(s)<2:
#             return False
        
#         for bracket in s:
#             if bracket in brackets.values(): 
#                 stack.append(bracket)
#             else:
#                 if not stack or brackets[bracket] != stack.pop():
#                     return False
#         if stack: 
#             return False
#         return True