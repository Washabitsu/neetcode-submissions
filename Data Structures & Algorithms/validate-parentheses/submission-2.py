class Solution:
    def isValid(self, s: str) -> bool:
        opposite_values ={
            '[':']',
            '{':'}',
            '(':')'
        }

        stack = []
        for i in s:
            if len(stack) != 0 and opposite_values.get(stack[-1],None) == i:
                stack.pop()
                continue
            stack.append(i)
        
        return  len(stack) == 0 