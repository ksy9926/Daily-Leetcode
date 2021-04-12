class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result = ""

        temp = list(map(lambda x: len(x), strs))
        
        if temp != []:
            for i in range(min(temp)):
                for j in range(1, len(strs)):
                    if strs[0][i] != strs[j][i]:
                        return result
                result += strs[0][i]

            return result
        else:
            return ""