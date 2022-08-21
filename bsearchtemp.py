class Solution:
    def mySqrt(self, x: int) -> int:
        if x<2:
            return x
        
        low, high = 0, x
        # for example if x is 36
        # mid is 18
        # 18*18 > 36, so we need to search the lower bound.
        
        # lets say that we have a case where our mid becomes 3
        # 3*3 is 9, and it is less than 36. increase our search bound
        while low < high:
            mid = low + (high - low) / 2
            print([low, high])
            print(mid)
            if mid*mid > x:
                high = mid
            elif mid*mid < x:
                low = mid
            else:
                return mid
        return int(mid)

if __name__ == "__main__":
    init = Solution()
    init.mySqrt(5)