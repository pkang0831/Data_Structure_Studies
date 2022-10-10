class BSearch:
    def __init__(self, inputList: list):
        self.inputList = inputList
        

    def bisect_left(self, target: int) -> int:
        left, right = 0, len(self.inputList) - 1

        while left < right:
            mid = (left + right) // 2
            
            if self.inputList[mid] < target:
                left = mid + 1
            else:
                right = mid
        return left

    def bisect_right(self, target: int) -> int:
        left, right = 0, len(self.inputList) - 1

        while left < right:
            mid = (left + right) // 2

            if self.inputList[mid] <= target:
                left = mid + 1
            else:
                right = mid
        return right

    def bisect_bisect(self, target: int) -> int:
        pass


# while left < right:
#             mid = (left + right) // 2

#             if self.inputList[mid] < target:
#                 # search right half
#                 left = mid + 1
#             elif self.inputList[mid] > target:
#                 # search left half
#                 right = mid
#             else:
#                 return mid
#         return -1

if __name__ == "__main__":
    T, F = True, False
    inputList = [2,3,4,5,6,7,7,7,8,9]
    condition = [T,T,T,T,T,F,F,F,F,F]
    indexList = [0,1,2,3,4,5,6,7,8,9]
    # bisect left returns the index 5 (checks if it is less than the target) < target
    # bisect right returns the index 8 (checks if it is less than or equal to target) <= target
    target = 7
    init = BSearch(inputList = inputList)
    target_index = init.bisect_left(7)
    target_index_right = init.bisect_right(7)
    print("bisect left: ", target_index)
    print("bisect right: ", target_index_right)