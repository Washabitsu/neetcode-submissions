
class Solution:

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for st in strs:
            tmp_arr = [0]*26
            for i in st:
                tmp_arr[ord(i)-97] += 1
            k = tuple(tmp_arr)
            if k in d:
                d[k].append(st)
                continue
            d[k] = [st]
        return list(d.values())
            
            