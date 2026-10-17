class DynamicArray:
    
    def __init__(self, capacity: int):
        self.arr = [None] * capacity
        self.current_index = 0

    def get(self, i: int) -> int:
        return self.arr[i]

    def set(self, i: int, n: int) -> None:
        self.arr[i] = n

    def pushback(self, n: int) -> None:
        if self.current_index == len(self.arr):
            self.resize()
        self.arr[self.current_index] = n
        self.current_index += 1

    def popback(self) -> int:
        self.current_index -= 1
        tmp = self.arr[self.current_index]
        self.arr[self.current_index] = None
        return tmp

    def resize(self) -> None:
        new_arr_allocation  = [None] * len(self.arr) * 2
        for i in range(self.current_index):
            new_arr_allocation[i] = self.arr[i]
        self.arr = new_arr_allocation

    def getSize(self) -> int:
        return self.current_index
    
    def getCapacity(self) -> int:
        return len(self.arr)