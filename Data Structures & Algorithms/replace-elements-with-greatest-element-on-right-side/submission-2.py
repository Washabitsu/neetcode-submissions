class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        m = arr[-1]
        arr[-1] = -1
        for i in range(1,len(arr)):
            if (arr[-1-i] > m):
                arr[-1-i],m = m,arr[-1-i]
                continue
            arr[-1-i] = m
        return arr