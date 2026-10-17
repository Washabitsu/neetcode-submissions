class Solution:
    def calPoints(self, operations: List[str]) -> int:
        s = []
        for v in operations:
            if v == "C":
                s.pop()
            elif v == "+":
                s.append(s[-1]+ s[-2])
            elif v == "D":
                s.append(s[-1]*2)
            else:
                s.append(int(v))
        
        total = 0
        for num in s:
            total += num
        
        return total
                
                 