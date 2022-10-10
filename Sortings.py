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
        # 
        self._quickSort(self.inputList, 0, len(self.inputList) - 1)
        return self.inputList
    
    def _quickSort(self, arr, start, end):

        if start >= end:
            return
        
        pivot = arr[end]
        p = start

        # 만약에, 피벗 정할때 맨 끄트머리가 아니고 랜덤으로 정하면, 그 정한 인덱스와 맨 끄트머리의 숫자를 먼저 바꿔주고 시작해야함.


        for i in range(start, end):
            if arr[i] <= pivot:
                # swap the element
                arr[i], arr[p] = arr[p], arr[i]
                p += 1
        # swap the pivot
        arr[p], arr[end] = arr[end], arr[p]
        # quicksort left
        self._quickSort(arr, start, p - 1)
        # quicksort right
        self._quickSort(arr, p + 1, end)

        # [2,5,7,3,8,45,6,87,1] ====> [....1,87] ====> [....87,6,1,45]
        # run1: pivot = 1, p = 0, end = 8
        # run1: forloop
        # [, , , , , ,1,5,7,3,8,45,6,87,2]

        # [1,      5,7,3,8,45,6,87,2]
        # run2: pivot = 2, p = 1, start = 1, end = 8
        # [1,2      ,7,3,8,45,6,87,5]

        # [1,2      ,7,3,8,45,6,87,5]
        # run3: pivot = 5, p = 2, start = 2, end = 8
        # forloop if condition 1: [1,2      ,3,7,8,45,6,87,5], p = 3, start = 2, end = 8
        # [1,2      ,3,5,8,45,6,87,7]

        # [1,2,3,5,      8,45,6,87,7]
        # run4: pivot: 7, p = 4, start = 4, end = 8
        # forloop if condition 1: [1,2,3,5,      6,45,8,87,7], p = 5, start = 4, end = 8
        # [1,2,3,5,6,7      ,8,87,45]

        # [1,2,3,5,6,7      ,8,87,45]
        # run 5: pviot: 45, p = 


if __name__ == "__main__":
    init = sorting([2,5,5,7,3,8,45,6,87,1])
    result = init.quickSort()
    print(result)