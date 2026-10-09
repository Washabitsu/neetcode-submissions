class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = len(nums)
        tr = [1]*l
        ls = 1 * nums[0]
        rs = 1 * nums[-1]
        for i in range(1,l):
            ri = l-1-i
            v = nums[i]
            vo = nums[ri]
            tr[i] *= ls
            tr[ri] *= rs
            ls *= v
            rs *= vo
        return tr