class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        i = 0
        tr = ""
        while(True):
            tc = ""
            for y,st in enumerate(strs):
                if i >= len(st):
                    return tr
                if y == 0:
                    tc = st[i]
                    continue
                if st[i] != tc:
                    return tr
            tr += tc
            i += 1
    