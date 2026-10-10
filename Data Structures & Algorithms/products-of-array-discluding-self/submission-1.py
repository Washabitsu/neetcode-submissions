class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = len(nums)
        tr = [1]*l
        ls = 1 * nums[0]
        rs = 1 * nums[-1]
        ac = False
        m = l // 2 if l % 2 == 0 else l // 2 + 1
        for i in range(1,l):
            ri = l-1-i
            v = nums[i]
            vo = nums[ri]
            tr[i] *= ls
            tr[ri] *= rs
            ls *= v
            rs *= vo
            # if ac :
            #     tr[i] *= ls
            #     tr[ri] *= rs
            # else:
            #     tr[i] *= ls 
            #     tr[ri] *= rs
            #     
                # if i == m:
                #     print(i,ls,rs,tr)
                #     ac = True
        return tr