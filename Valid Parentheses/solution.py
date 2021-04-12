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
                