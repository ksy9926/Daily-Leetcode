class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        if s == "" or s == " ":
            return 0
        temp = s.split(" ")
        
        while temp[-1] == "":
            if len(temp) > 1:
                temp.pop()
            else:
                break
        return len(temp[-1])