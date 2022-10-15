class backTrackingTutorial:
    def __init__(self, inputList: list):
        self.input = inputList
        self.result = []

    def dfsPermute(self):
        self._dfsPermute([], self.input)
        print(self.result)
        return self.result

    def _dfsPermute(self, tempList: list,  inputList: list):
        if len(inputList) == 0:
            self.result.append(tempList[:])

        for idx in range(len(inputList)):
            tempList.append(inputList[idx])
            # Backtrack
            nextElements = inputList[:idx] + inputList[idx + 1 :]
            self._dfsPermute(tempList, nextElements)
            tempList.pop()


if __name__ == "__main__":
    init = backTrackingTutorial([1,2,2])
    init.dfsPermute() 