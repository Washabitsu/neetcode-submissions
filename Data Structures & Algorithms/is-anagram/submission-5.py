class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        def a_or_i(d, v, t):
            if t is None:
                if v in d.keys():
                    d[v] += 1
                    return
                d[v] = 1
                return
            if v not in d.keys():
                d[v] = {}
            return a_or_i(d[v],t,None)
            
        a = {}
        s_l = len(s)
        if s_l != len(t):
            return False
        for i in range(0,s_l):
            a_or_i(a,s[i], "s")
            a_or_i(a,t[i], "t")
        
        for key in a:
            k = a[key].keys()
            if "s" in a[key] and "t" in a[key]:
                if a[key]["s"] != a[key]["t"]:
                    return False
                continue
            return False
        return True
            

