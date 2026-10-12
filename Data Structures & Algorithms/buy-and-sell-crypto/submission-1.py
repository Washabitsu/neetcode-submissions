class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        _min = prices[0]
        _max = 0
        profit = 0
        for i in prices:
            if i < _min:
                _min = i
                _max = 0    
            elif i > _max:
                _max = i
            if _max - _min > profit:
                profit = _max - _min
        return profit