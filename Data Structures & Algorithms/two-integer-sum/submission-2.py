class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l = len(nums)
        if l == 2:
            return [0,1]

        d = {}
        d[nums[0]] = 0
        for i in range(1,l):
            tmp = d.get(target -nums[i] ,None)
            if tmp is not None:
                return [tmp, i]
            d[nums[i]] = d.get(nums[i],i)

        
                

            

