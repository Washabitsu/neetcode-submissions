class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        m = arr[-1]
        arr[-1] = -1
        for i in range(1,len(arr)):
            arr[-1-i], m = m, max(arr[-1-i],m)
        return arr