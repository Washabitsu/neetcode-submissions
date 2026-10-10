class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        l = len(strs[0])
        i = 0
        while(True):
            for st in strs:
                tr = strs[0][0:i]
                if len(st) < i:
                    return st[0:i-1]
                    
                if st[0:i] != tr:
                    if i != 0:
                        return st[0:i-1]
                    return ""
            i += 1
    