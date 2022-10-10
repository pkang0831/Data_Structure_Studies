class sorting:
    def __init__(self, inputList: list):
        self.inputList = inputList

    def mergeSort(self):
        # mergesort explanation:
        # lets say that you have unsorted array [2,5,7,3,8,45,6,87,1]
        # what you do is you keep dividing in half and sort left and right using DFS algorithms.
        self._mergeSort(self.inputList)
        return self.inputList

    def _mergeSort(self, arr):
        if len(arr) > 1:
            
            # partition the array
            mid = len(arr) // 2

            leftList = arr[:mid]
            rightList = arr[mid:]

            self._mergeSort(leftList)
            self._mergeSort(rightList)

            leftIdx = rightIdx = arrIdx = 0
            
            while leftIdx < len(leftList) and rightIdx < len(rightList):
                if leftList[leftIdx] <= rightList[rightIdx]:
                    arr[arrIdx] = leftList[leftIdx]
                    leftIdx += 1
                else:
                    arr[arrIdx] = rightList[rightIdx]
                    rightIdx += 1
                arrIdx += 1

            while leftIdx < len(leftList):
                arr[arrIdx] = leftList[leftIdx]
                leftIdx += 1
                arrIdx += 1

            while rightIdx < len(rightList):
                arr[arrIdx] = rightList[rightIdx]
                rightIdx += 1
                arrIdx += 1


    def quickSort(self):
        pass

if __name__ == "__main__":
    init = sorting([2,5,5,7,3,8,45,6,87,1])
    result = init.mergeSort()
    print(result)