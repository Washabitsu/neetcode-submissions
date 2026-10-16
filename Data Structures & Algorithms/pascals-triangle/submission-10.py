class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        to_return = [[1]]
        for _ in range(1,numRows):
            cv = to_return[-1]
            cv_length = len(cv)
            sub_array = [1]
            for y in range(1, cv_length):
                sub_array.append(cv[y] + cv[y-1])

            sub_array.append(1)
            to_return.append(sub_array)
        return to_return