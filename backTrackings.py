import collections
class Solution:
    def __init__(self, inputList: list, months: int):
        self.monthLimit = months
        self.inputList = inputList
        self.tempDict = collections.defaultdict(list)
        self.invTempDict = collections.defaultdict(str)
        self.curMax = float('-inf')
        self.bestCombin = []

        def hashMaps():
            """store the inputlist to product:(duration, profit)"""
            for prod, profits in self.inputList:
                self.tempDict[prod] = [(len(prod), profits/len(prod))]
                
            for key, val in self.tempDict.items():
                self.invTempDict[val[0][0]] = val[0][1]
        hashMaps()


    def dfs(self, nums, path, ret):

        if sum(path) > self.monthLimit:
            possiblePath = path[:-1]
            curSum = 0
            for i in possiblePath:
                curSum += self.invTempDict[i]
            
            if curSum > self.curMax:
                self.curMax = curSum
                self.bestCombin = possiblePath

            return

        for i in range(len(nums)):
            self.dfs(nums[i:], path+[nums[i]], ret)

    def combinationPaths(self):
        ret = []
        prodLengths = [val[0][0] for key, val in self.tempDict.items()]
        self.dfs(prodLengths, [], ret)
        print(self.curMax)
        print(self.bestCombin)
        return ret


if __name__ == "__main__":
    inputList = [
            ('aaa', 1),
            ('abcdefgh', 3),
            ('abcde', 2)
        ]
    init = Solution(inputList, 20)
    solu = init.combinationPaths()


    # Time complexity: O(k^n)
    # Space complexity: O(N)