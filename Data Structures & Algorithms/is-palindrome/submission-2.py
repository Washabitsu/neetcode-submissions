class Solution:
    def isPalindrome(self, s: str) -> bool:
        ## Could be done also with regex
        def isAlpha(num, tuple_range:List[tuple]):
            for _tuple in tuple_range:
                if num >= _tuple[0] and num <= _tuple[1]:
                    return True
            return False
        
        ranges = [(ord('a'),ord('z')),(ord('A'),ord('Z')),(ord('0'),ord('9'))]
        middle = len(s) // 2
        l_index = 0
        r_index = 0
        while(l_index < len(s) and r_index < len(s)):
            while l_index < len(s)-1 and isAlpha(ord(s[l_index]),ranges) == False:
                l_index += 1
            while r_index < len(s)-1 and isAlpha(ord(s[-1-r_index]),ranges) == False :
                print(r_index)
                r_index += 1

            if l_index >= middle and r_index >= middle:
                return True

            if s[l_index].lower() != s[-1-r_index].lower():
                return False

            l_index += 1
            r_index += 1

        return True

            