class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        _min = prices[0]
        _max = 0
        profit = 0
        for i in prices:
            if i < _min:
                t_profit = _max - _min
                if t_profit > profit:
                    profit = t_profit
                _min = i
                _max = 0
                
            elif i > _max:
                _max = i
        t_profit = _max - _min
        if t_profit > profit:
            return t_profit
        return profit