class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        to = dict()
        for i in nums:
            if i in to.keys():
                return True
            to[i] = 1
        return False