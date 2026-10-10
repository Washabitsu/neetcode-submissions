class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        i = 0
        while(True):
            for y,st in enumerate(strs):
                if i >= len(st):
                    return st[0:i]
                if strs[0][i] != st[i]:
                    return st[0:i]
            i += 1
    