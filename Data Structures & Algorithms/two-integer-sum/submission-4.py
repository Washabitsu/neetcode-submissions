class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        d[nums[0]] = 0
        for i in range(1,len(nums)):
            tmp = d.get(target -nums[i] ,None)
            if tmp is not None:
                return [tmp, i]
            d[nums[i]] = i

        
                

            

