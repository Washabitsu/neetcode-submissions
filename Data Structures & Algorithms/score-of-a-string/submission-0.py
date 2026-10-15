class Solution:
    def scoreOfString(self, s: str) -> int:
        total_value = 0
        for i in range(1,len(s)):
            total_value += abs(ord(s[i]) - ord(s[i-1]))
        return total_value
