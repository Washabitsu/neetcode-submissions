class Solution:

    def encode(self, strs: List[str]) -> str:
        # Concat string with length of word and $ as delimeter  
        s = ""
        for st in strs:
            s += str(len(st)) + "$" + st
        print(s)
        return s

    
    def decode(self, s: str) -> List[str]:
        wtr = []
        cn = ""
        i = 0
        while i < len(s):
            if s[i] == "$":
                length = int(cn)
                wtr.append(s[i+1 : i+1+length])
                cn = ""
                i = i + 1 + length    # lands on the next header's first digit
            else:
                cn += s[i]
                i += 1
        return wtr
