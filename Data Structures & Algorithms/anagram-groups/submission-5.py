import ctypes

class Solution:

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        tr = []
        for st in strs:
            tmp_arr = [0]*26
            for i in st:
                tmp_arr[ord(i)-97] += 1
            k = hash(tuple(tmp_arr))
            if k in d.keys():
                d[k].append(st)
                continue
            n_a = [st]
            d[k] = n_a
            tr.append(n_a)

        return tr
            
            