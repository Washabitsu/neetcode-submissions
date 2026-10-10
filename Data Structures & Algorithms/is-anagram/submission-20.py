class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        l = len(s)
        if l != len(t):
            return False

        arr = [0] * 26
        arr2 = [0] * 26
        for sv in s:
            arr[ord(sv) - ord('a')] += 1
        for tv in t:
            arr2[ord(tv) - ord('a')] += 1
        return arr == arr2