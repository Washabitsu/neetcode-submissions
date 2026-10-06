class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        l = len(s)
        if l != len(t):
            return False

        a = [0] * 26
        for i in range(0,l):
            a[ord(s[i].lower()) - 97] += 1
            a[ord(t[i].lower()) - 97] -= 1

        for i in a:
            if i != 0:
                return False
        return True

        