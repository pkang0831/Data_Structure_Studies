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
                self.tempDict[prod] = [(len(prod), profits)]

            for key, val in self.tempDict.items():
                self.invTempDict[val[0][0]] = key
        hashMaps()
        print(self.tempDict)
        print(self.invTempDict)


    def dfs(self, nums, path, ret):

        if sum(path) > self.monthLimit:
            return 

        ret.append(path)

        # curSum = sum(ret)

        # if curSum > self.curMax:
        #     self.curMax = curSum
        #     self.bestCombin = ret

        for i in range(len(nums)):
            self.dfs(nums[i:], path+[nums[i]], ret)

    def combinationPaths(self):
        ret = []
        prodLengths = [val[0][0] for key, val in self.tempDict.items()]
        self.dfs(prodLengths, [], ret)
        print(ret)
        print(self.curMax)
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